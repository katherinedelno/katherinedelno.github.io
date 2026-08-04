#!/usr/bin/env python3
"""
Generate Open Graph social cards for every post, and a default card for pages.

Cards are 1200x630 PNGs written to /assets/og/<slug>.png, drawn in the site's
own typography (Hanken Grotesk, ink #1f1f1f, the 18x2 accent rule that precedes
every .label on the site).

The script also writes `image: "/assets/og/<slug>.png"` into each post's front
matter, which is what jekyll-seo-tag reads. Setting page.image makes seo-tag
emit og:image and switch the Twitter card from `summary` to
`summary_large_image` automatically.

Idempotent: safe to re-run after adding posts. Existing `image:` lines are
rewritten rather than duplicated.

    python3 tools/og-cards.py            # generate everything
    python3 tools/og-cards.py --no-write # cards only, leave front matter alone
"""

import glob
import os
import re
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, "tools", "fonts")
OUT = os.path.join(ROOT, "assets", "og")

W, H = 1200, 630
MARGIN = 84

INK = (31, 31, 31)
MUTED = (92, 92, 92)
LINE = (230, 230, 230)
BG = (255, 255, 255)

PAGES = [
    ("readiness-calculus",
     "Are you ready for AP Calculus?",
     "Diagnostic",
     "Sixteen questions in the algebra, functions, and trigonometry the course assumes."),
]

BOLD = os.path.join(FONTS, "HankenGrotesk-700-normal.ttf")
SEMI = os.path.join(FONTS, "HankenGrotesk-600-normal.ttf")
REG = os.path.join(FONTS, "HankenGrotesk-400-normal.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def track(draw, xy, text, f, fill, spacing):
    """Draw text with extra letter-spacing, the way the site's .label sets it."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=f, fill=fill)
        x += draw.textlength(ch, font=f) + spacing
    return x


def wrap(draw, text, f, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if draw.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def card(title, eyebrow, blurb, path):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Hairline frame, echoing the 1px borders used across the site's cards.
    d.rectangle([0, 0, W - 1, H - 1], outline=LINE, width=1)

    # Eyebrow: the 18x2 accent rule, then uppercase tracked-out course name.
    if eyebrow:
        d.rectangle([MARGIN, MARGIN + 9, MARGIN + 18, MARGIN + 11], fill=INK)
        track(d, (MARGIN + 29, MARGIN), eyebrow.upper(), font(SEMI, 20), INK, 2.6)

    # Footer rule and wordmark.
    fy = H - MARGIN - 30
    d.rectangle([MARGIN, fy, W - MARGIN, fy + 1], fill=LINE)
    d.text((MARGIN, fy + 17), "katherinedelno.com", font=font(REG, 22), fill=MUTED)

    # Title and blurb form one block anchored to the footer rule, so the card
    # grows upward with the title instead of stranding short titles mid-air.
    max_w = W - 2 * MARGIN
    ceiling = MARGIN + (54 if eyebrow else 0)
    floor = fy - 46

    bf = font(REG, 26)
    for size in (64, 58, 52, 47, 43, 39):
        tf = font(BOLD, size)
        tlines = wrap(d, title, tf, max_w)
        leading = int(size * 1.13)
        blines = wrap(d, blurb, bf, max_w)[:2] if blurb else []
        block = len(tlines) * leading + (len(blines) * 36 + 16 if blines else 0)
        if block <= floor - ceiling:
            break

    y = floor - block
    for ln in tlines:
        d.text((MARGIN, y), ln, font=tf, fill=INK)
        y += leading
    if blines:
        y += 16
        for ln in blines:
            d.text((MARGIN, y), ln, font=bf, fill=MUTED)
            y += 36

    img.save(path, "PNG", optimize=True)


def front_matter(src):
    parts = src.split("---\n", 2)
    return (parts[1], parts[2]) if len(parts) >= 3 else (None, None)


def field(fm, key):
    m = re.search(rf'^{key}:\s*"?(.*?)"?\s*$', fm, re.M)
    return m.group(1) if m else None


def main():
    write_fm = "--no-write" not in sys.argv
    os.makedirs(OUT, exist_ok=True)

    card("Mathematics and statistics, taught one student at a time.",
         "Private instruction",
         "One-on-one teaching in AP Statistics, AP Calculus, and AP Precalculus.",
         os.path.join(OUT, "default.png"))

    # Standalone pages that want their own card. Add a line here when you add a
    # page whose front matter names an /assets/og/<slug>.png.
    for slug, title, eyebrow, blurb in PAGES:
        card(title, eyebrow, blurb, os.path.join(OUT, f"{slug}.png"))

    n = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "_posts", "*.md"))):
        src = open(path, encoding="utf-8").read()
        fm, body = front_matter(src)
        if fm is None:
            print(f"  skipped (no front matter): {os.path.basename(path)}")
            continue

        title = field(fm, "title")
        if not title:
            print(f"  skipped (no title): {os.path.basename(path)}")
            continue

        slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", os.path.basename(path))[:-3]
        rel = f"/assets/og/{slug}.png"
        card(title, field(fm, "course") or "", field(fm, "blurb") or "",
             os.path.join(OUT, f"{slug}.png"))
        n += 1

        if write_fm:
            if re.search(r"^image:", fm, re.M):
                fm2 = re.sub(r'^image:.*$', f'image: "{rel}"', fm, flags=re.M)
            else:
                fm2 = fm.rstrip("\n") + f'\nimage: "{rel}"\n'
            if fm2 != fm:
                open(path, "w", encoding="utf-8").write(f"---\n{fm2}---\n{body}")

    print(f"wrote {n} post cards + default.png to assets/og/")
    if write_fm:
        print("front matter updated with image: paths")


if __name__ == "__main__":
    main()

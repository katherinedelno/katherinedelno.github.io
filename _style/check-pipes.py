#!/usr/bin/env python3
"""Superseded by _style/check.py, which runs this check and every other one.

Kept as a stub so nothing that referenced it breaks. Delete it whenever.
"""
import sys, os, subprocess
here = os.path.dirname(os.path.abspath(__file__))
sys.exit(subprocess.call([sys.executable, os.path.join(here, 'check.py')] + sys.argv[1:]))

#!/usr/bin/env python3
"""Entry for make.fun bounty news-image-20261117.

Writes one image summing up Tuesday 17 November 2026's world news to
/output/entry.png. The image is baked into this repository (entry.png) and
this program copies it to the output path, as the bounty brief allows:
"the simplest program copies an image the repository holds".
The image was rendered by build_image.py (PIL) from the verified headlines
of 17 November 2026; see README.md for the stories and sources.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main() -> int:
    if not os.path.isfile(SRC):
        print(f"entry.png not found next to {__file__}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    print(f"wrote {DST} ({os.path.getsize(DST)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

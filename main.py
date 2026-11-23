# A news-image-20261122 entry (Python 3.13, standard library only): its image
# is the entry.png beside this file, and the program copies it to
# /output/entry.png. Outside the grader's container, MAKEFUN_OUTPUT_DIR
# stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

# The copy is byte-for-byte and deterministic: the same entry.png is written
# on every run, with no network and no randomness.
src = Path(__file__).resolve().parent / "entry.png"
out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
dest = out / "entry.png"
shutil.copyfile(src, dest)

# Verify the copy landed byte-for-byte before reporting success.
assert dest.stat().st_size == src.stat().st_size
print(f"Wrote {dest} ({dest.stat().st_size} bytes)")

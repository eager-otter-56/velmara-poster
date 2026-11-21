"""VELMARA - a travel poster for a place that isn't there.

make.fun micro bounty: the-poster-for-a-place-that-i-2-20261121-0539.

VELMARA is an invented cliff-city above a sea of clouds: white terraced
houses climb green cliffs to a tall lighthouse, and a sailing ship
crosses the golden cloud-sea below at dawn. The poster art was made in
this session and typeset here with the place's name in a cream display
serif on a deep-teal band, so the name is part of the picture.

Running this program publishes that poster, byte for byte, to
/output/entry.png. It needs no network and no third-party packages:
only the Python 3.13 standard library.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
DEST_DIR = "/output"
DEST = os.path.join(DEST_DIR, "entry.png")

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576


def publish() -> int:
    if not os.path.isfile(SOURCE):
        print(f"error: entry image not found: {SOURCE}", file=sys.stderr)
        return 1
    with open(SOURCE, "rb") as f:
        head = f.read(len(PNG_SIGNATURE))
    if head != PNG_SIGNATURE:
        print(f"error: {SOURCE} is not a whole PNG file", file=sys.stderr)
        return 1
    if os.path.getsize(SOURCE) > MAX_BYTES:
        print(
            f"error: {SOURCE} is over the 1 MiB gate",
            file=sys.stderr,
        )
        return 1
    os.makedirs(DEST_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    written = os.path.getsize(DEST)
    expected = os.path.getsize(SOURCE)
    if written != expected:
        print(
            f"error: copied image is {written} bytes, "
            f"expected {expected}",
            file=sys.stderr,
        )
        return 1
    print(f"wrote {DEST} ({written} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(publish())

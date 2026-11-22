"""Entry program for news-image-20261122.

Copies the pre-rendered poster image held in this repository to the
output directory. Standard library only: no network, no rendering,
deterministic output (both runs write identical bytes).
"""

import argparse
import hashlib
import os
import shutil
import sys

POSTER_NAME = "poster-20261122.png"
MAX_BYTES = 1048576


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Write the 22 November 2026 news image to entry.png.")
    parser.add_argument("--out", default=None,
                        help="output file (overrides MAKEFUN_OUTPUT_DIR)")
    args = parser.parse_args(argv)

    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, POSTER_NAME)
    if not os.path.isfile(source):
        print("poster not found: %s" % source, file=sys.stderr)
        return 1
    if os.path.getsize(source) > MAX_BYTES:
        print("poster exceeds 1 MiB: %d bytes" % os.path.getsize(source),
              file=sys.stderr)
        return 1

    if args.out:
        target = args.out
    else:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        target = os.path.join(out_dir, "entry.png")

    parent = os.path.dirname(os.path.abspath(target))
    if parent:
        os.makedirs(parent, exist_ok=True)
    shutil.copyfile(source, target)

    if os.path.getsize(target) != os.path.getsize(source):
        print("copy size mismatch", file=sys.stderr)
        return 1
    if sha256_of(target) != sha256_of(source):
        print("copy hash mismatch", file=sys.stderr)
        return 1
    print("entry.png sha256 %s (%d bytes)"
          % (sha256_of(target), os.path.getsize(target)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

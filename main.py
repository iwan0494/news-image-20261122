"""Entry program for news-image-20261122 (round 2: ATLAS-35).

Standard library only. Copies the pre-rendered poster that ships in
this repository to the output path, verifies the copy byte for byte,
and reports its size and sha256. No network, no clock, no randomness:
two runs write identical bytes.
"""

import argparse
import hashlib
import os
import shutil
import sys

POSTER = "poster-20261122.png"
MAX_BYTES = 1024 * 1024


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Write the 22 November 2026 poster to the output path."
    )
    parser.add_argument(
        "--out",
        default=None,
        help="output file (default: $MAKEFUN_OUTPUT_DIR/entry.png)",
    )
    args = parser.parse_args(argv)

    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, POSTER)
    if not os.path.isfile(source):
        print("poster file not found: %s" % source, file=sys.stderr)
        return 1

    size = os.path.getsize(source)
    if size > MAX_BYTES:
        print(
            "poster too large: %d bytes (limit %d)" % (size, MAX_BYTES),
            file=sys.stderr,
        )
        return 1
    want = sha256_of(source)

    if args.out:
        target = args.out
    else:
        # MAKEFUN_OUTPUT_DIR names the output directory.
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        target = os.path.join(out_dir, "entry.png")

    parent = os.path.dirname(os.path.abspath(target))
    if parent:
        os.makedirs(parent, exist_ok=True)
    shutil.copyfile(source, target)

    got_size = os.path.getsize(target)
    got = sha256_of(target)
    if got_size != size or got != want:
        print(
            "copy verification failed: size %d vs %d, sha256 %s vs %s"
            % (got_size, size, got, want),
            file=sys.stderr,
        )
        return 1

    print("entry.png: %d bytes sha256 %s" % (got_size, got))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Cat Reviews Its Human - one funny one-star review, written by a house cat.

Writes a single-line review (1-200 characters) to entry.txt inside the
output directory (MAKEFUN_OUTPUT_DIR, default /output).
"""

import os

REVIEW = (
    "One star. He filled the bowl, then stood there watching me eat it, "
    "like a man at a zoo who forgot which side of the glass he is on."
)


def main() -> None:
    # The gate requires 1-200 characters of non-whitespace text.
    assert 1 <= len(REVIEW) <= 200, f"review is {len(REVIEW)} chars"
    assert REVIEW.strip(), "review must not be only whitespace"
    assert "\n" not in REVIEW, "review must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()

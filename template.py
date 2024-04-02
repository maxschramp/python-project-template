#!/usr/bin/env python
# template courtesy of https://adamj.eu/tech/2021/10/09/a-python-script-template-with-and-without-type-hints-and-async/

from __future__ import annotations

import argparse
from collections.abc import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    # Add arguments here
    args = parser.parse_args(argv)

    # Implement behaviour here

    return 0


if __name__ == "__main__":

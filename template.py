#!.\venv\Scripts\python.exe
# template courtesy of https://adamj.eu/tech/2021/10/09/a-python-script-template-with-and-without-type-hints-and-async/

from __future__ import annotations

import argparse
import os
from collections.abc import Sequence

from colorama import Fore, Style
from dotenv import dotenv_values


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    # Add arguments here (https://docs.python.org/3/library/argparse.html)
    # parser.add_argument("--name", type=str, required=True, nargs=1)
    args = parser.parse_args(argv)

    # load variables from .env file
    global env
    env = dotenv_values(f"{os.path.dirname(os.path.realpath(__file__))}\\.env")

    # Start writing code here

    print(Style.RESET_ALL)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

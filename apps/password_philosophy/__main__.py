import argparse
from libs.password_philosophy import main

PASSWORD_PHILOSOPHY_DEFAULT_INPUT: str = "libs/password_philosophy/data/input.txt"

ARGS = argparse.ArgumentParser(description=main.__doc__)
ARGS.add_argument(
    "--input_file",
    type=str,
    default=PASSWORD_PHILOSOPHY_DEFAULT_INPUT,
    help="A text file with newline delimited password policies.",
)

if __name__ == "__main__":
    args = ARGS.parse_args()
    main(input_file=args.input_file)

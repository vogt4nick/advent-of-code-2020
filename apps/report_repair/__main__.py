import argparse
from libs.report_repair import main

REPORT_REPAIR_DEFAULT_INPUT: str = "libs/report_repair/data/input.txt"

ARGS = argparse.ArgumentParser(description=main.__doc__)
ARGS.add_argument(
    "--input_file",
    type=str,
    default=REPORT_REPAIR_DEFAULT_INPUT,
    help="A text file with newline delimited integers.",
)


if __name__ == "__main__":
    args = ARGS.parse_args()
    main(input_file=args.input_file)

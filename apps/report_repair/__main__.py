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
ARGS.add_argument(
    "--n_addends",
    type=int,
    default=2,
    help="The number of addends used to calculate the sum.",
)
ARGS.add_argument(
    "--sum",
    type=int,
    dest="sum_",
    default=2020,
    help="The number to which the addends should sum.",
)


if __name__ == "__main__":
    args = ARGS.parse_args()
    main(input_file=args.input_file, n_addends=args.n_addends, sum_=args.sum_)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
from libs.password_philosophy import PASSWORD_PHILOSOPHY_DEFAULT_INPUT, main


ARGS = argparse.ArgumentParser(description=main.__doc__)
ARGS.add_argument(
    "--input_file",
    type=str,
    default=PASSWORD_PHILOSOPHY_DEFAULT_INPUT,
    help="A text file with newline delimited password policies.",
)
ARGS.add_argument(
    "--policy_type",
    type=str,
    help="The policy type to interpret the policy string. One of 'count' or 'index'.",
)

if __name__ == "__main__":
    args = ARGS.parse_args()
    main(input_file=args.input_file, policy_type=args.policy_type)

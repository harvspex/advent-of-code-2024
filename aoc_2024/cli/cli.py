import argparse
from aoc_2024.day_class.day_factory import run_day
from aoc_2024.cli.validation import valid_day_int, readable_file

def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='Advent of code 2024!'
    )
    parser.add_argument(
        'day',
        help='the day number to run',
        type=valid_day_int
    )
    parser.add_argument(
        '-p', '--part',
        help='which part of day to run',
        type=int,
        choices=[1,2],
        default=None
    )
    parser.add_argument(
        '-i', '--input',
        help='specify input file for day',
        type=readable_file
    )
    parser.add_argument(
        '-t', '--test',
        help='run day using test input',
        action='store_true'
    )
    parser.add_argument(
        '-q', '--quiet',
        help='run without printing results',
        action='store_true',
        default=False
    )

    return parser

def handle_args(args: argparse.Namespace):
    run_day(
        day_num=args.day,
        part_num=args.part,
        infile=args.input,
        test_mode=args.test,
        verbose=not args.quiet
    )

def main():
    parser = get_parser()
    args = parser.parse_args()
    handle_args(args)

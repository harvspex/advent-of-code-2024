from typing import Any
from aoc_2024.day_class.day import Day
from aoc_2024.days.day_1 import Day1

def get_day(day: int) -> type:
    day_type: type = None

    match day:
        case 1:
            day_type = Day1
        case _:
            raise ValueError(f'Day {day} does not exist!')

    return day_type


def run_part(day_class: Day, part: int=None):
    result: Any = None
    match part:
        case 1:
            result = day_class.part_1()
        case 2:
            result = day_class.part_2()
        case _:
            raise ValueError(f'Day {day_class} part {part} does not exist!')

    return result


def get_input(filename: str) -> str:
    INPUT_PATH: str = 'aoc_2024/inputs/'
    DAY: str = 'day_'
    EXT: str = '.txt'

    if filename.isdigit():
        filename = f'{INPUT_PATH}{DAY}{filename}{EXT}'

    return filename


def print_result(result: Any, day: int, part: int):
    print(f'Day {day} part {part}: {result}')


def run_day(day: int, *parts: int, input_file: str=None, verbose:bool=True):
    if input_file is None:
        input_file = str(day)

    day_type: type = get_day(day)
    infile: str = get_input(input_file)

    try:
        day_class: Day = day_type(infile)

    except FileNotFoundError:
        print('That file does not exist or cannot be read.')

    for part in parts:
        result: Any = run_part(day_class, part)

        if verbose:
            print_result(result)

        yield result

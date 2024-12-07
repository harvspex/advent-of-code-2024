from aoc_2024.day_class.day import Day
from aoc_2024.days.day_1 import Day1
from aoc_2024.days.day_2 import Day2

DAYS_DICT = {
    1: Day1,
    2: Day2,
}

def get_filename(filename: str, test_mode: bool=False) -> str:

    if filename.isdigit():
        if test_mode:
            filename = f'aoc_2024/test_inputs/day_{filename}.txt'
        else:
            filename = f'aoc_2024/inputs/day_{filename}.txt'

    return filename

def run_day(
        day_num: int,
        part_num: int=None,
        infile: str=None,
        test_mode: bool=False,
        verbose: bool=True,
        days_dict: dict[int, Day]=DAYS_DICT
    ):
    if day_num not in days_dict:
        raise ValueError(f'Day {day_num} does not exist.')

    # Prepare input filename
    if infile is None:
        infile = get_filename(str(day_num), test_mode)

    # Create day
    day_type: type = days_dict[day_num]
    day_class: Day = day_type(infile)

    # Run part/s of day
    day_class.run(
        day_num=day_num,
        part_num=part_num,
        verbose=verbose
    )
import importlib
import os
import re
from aoc_2024.day_class.day import Day

def discover_days(directory: str="aoc_2024/days") -> dict[int, type]:
    days_dict = {}
    day_pattern = re.compile(r"day_(\d+)\.py$")  # Matches files like day_1.py, day_2.py

    for filename in os.listdir(directory):
        match = day_pattern.match(filename)
        if match:
            day_num = int(match.group(1))
            module_name = f"aoc_2024.days.{filename[:-3]}"  # Remove ".py" from filename
            module = importlib.import_module(module_name)

            # Get the class from the module (assumes class is named `DayX`)
            class_name = f"Day{day_num}"
            day_class = getattr(module, class_name, None)

            if day_class and issubclass(day_class, Day):  # Ensure it's a subclass of `Day`
                days_dict[day_num] = day_class

    return days_dict

# Dynamically populate DAYS_DICT
DAYS_DICT = discover_days()

def get_filename(filename: str, part_num: int=None, test_mode: bool=False) -> str:
    # TODO: Could be better. Will crash on bad part_num
    if filename.isdigit():
        if test_mode:
            filename = f'aoc_2024/test_inputs/day_{filename}'
            filename += f'_{part_num}.txt' if (part_num is not None) else '.txt'
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
        infile = get_filename(str(day_num), part_num, test_mode)

    # Create day
    day_type: type = days_dict[day_num]
    day_class: Day = day_type(infile)

    # Run part/s of day
    day_class.run(
        day_num=day_num,
        part_num=part_num,
        verbose=verbose
    )
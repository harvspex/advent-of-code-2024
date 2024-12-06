from typing import Any
from aoc_2024.day_class.day import Day
from aoc_2024.days.day_1 import Day1

DAYS = {
    1: Day1
}

def run_day(day: int, part: int=None, input_file: str=None, verbose:bool=True, days=DAYS):
    # Prepare input filename
    if input_file is None:
        input_file = str(day)

    # Get day object
    day_class: Day = days[day](input_file)

    # Run parts
    day_class.run(part)
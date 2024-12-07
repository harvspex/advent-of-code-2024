from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

@dataclass
class Day(ABC):
    infile: str

    @abstractmethod
    def part_1(self): ...

    @abstractmethod
    def part_2(self): ...

    def run(self, day_num: int, part_num: int=None, verbose: bool=True):
        result: Any = None

        match part_num:
            case None:
                # Run and return both parts as a tuple
                result = (
                    self.run(day_num, 1, verbose),
                    self.run(day_num, 2, verbose)
                )
                return result
            case 1:
                result = self.part_1()
            case 2:
                result = self.part_2()

        if verbose:
            print(f'Day {day_num} part {part_num}: {result}')

        return result

    def get_input(self):
        with open(self.infile, 'r') as infile:
            for line in infile:
                yield line
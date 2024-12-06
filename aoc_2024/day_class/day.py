from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

@dataclass
class Day(ABC):
    day_num: int

    @abstractmethod
    def part_1(self): ...

    @abstractmethod
    def part_2(self): ...

    def run(self, part=None):
        result: Any = None

        match part:
            case None:
                result = self.run(1), self.run(2)
                return result
            case 1:
                result = self.part_1()
            case 2:
                result = self.part_2()

        self.print_result(result, part)
        return result

    def print_result(self, result: Any, part: int):
        print(f'Day {self.day_num} part {part}: {result}')

    def get_filename(self) -> str:
        return f'aoc_2024/inputs/day_{self.day_num}.txt'

    def get_input(self, filename: str=None):
        if filename is None:
            filename = self.get_filename()

        with open(filename, 'r') as infile:
            for line in infile:
                yield line
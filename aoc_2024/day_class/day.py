from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Day(ABC):
    infile: str

    @abstractmethod
    def part_1(self): ...

    @abstractmethod
    def part_2(self): ...

    def get_input(filename: str):
        with open(filename, 'r') as infile:
            yield infile.readlines()
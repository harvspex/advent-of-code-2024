from dataclasses import dataclass, field
from functools import total_ordering
from aoc_2024.day_class.day import Day

@dataclass
# @total_ordering
class PageOrder:
    num: int
    before: list[int] = field(default_factory=list)
    after: list[int] = field(default_factory=list)

    # def __eq__(self, other):
    #     if isinstance(other, PageOrder):
    #         return self.num == other.num
    #     elif isinstance(other, int):
    #         return self.num == other
    #     elif isinstance(other, str):
    #         return str(self.num) == other
    #     else:
    #         return NotImplemented

    # def __gt__(self, other):
    #     if isinstance(other, PageOrder):
    #         # TODO: Test this
    #         return (self.num in other.after) or (self.num not in other.before)
    #     elif isinstance(other, int):
    #         return self.num > other
    #     elif isinstance(other, str):
    #         return str(self.num) > other
    #     else:
    #         return NotImplemented


class Day5(Day):
    def part_1(self):
        self.get_input()

    def get_input(self):
        page_orders: dict[PageOrder] = {}

        for line in super().get_input():
            try:
                before, after = [int(_) for _ in line.strip().split('|') if _.isdigit()]
                Day5.add_page_orders(before, after, page_orders)
            except ValueError as e:
                # TODO: Complete
                break

        print(page_orders.keys())

    @staticmethod
    def add_page_orders(before: int, after: int, page_orders: dict[PageOrder]):
        Day5.add_one_page(before, after, page_orders, before_mode=True)
        Day5.add_one_page(after, before, page_orders, before_mode=False)
        
    @staticmethod
    def add_one_page(
        page_a: int,
        page_b: int,
        page_orders: dict[PageOrder],
        before_mode: bool=True
    ):
        try:
            page: PageOrder = page_orders[page_a]
        except KeyError:
            page = PageOrder(page_a)
            page_orders[page_a] = page

        page_list = page.before if before_mode else page.after
        page_list.append(page_b)

    def part_2(self):
        pass
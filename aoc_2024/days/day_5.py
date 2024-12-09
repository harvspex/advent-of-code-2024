from dataclasses import dataclass, field
from functools import total_ordering
from aoc_2024.day_class.day import Day

@dataclass
@total_ordering
class PageOrder:
    num: int
    before: list[int] = field(default_factory=list)
    after: list[int] = field(default_factory=list)

    def __eq__(self, other):
        if isinstance(other, PageOrder):
            return self.num == other.num
        elif isinstance(other, int):
            return self.num == other
        elif isinstance(other, str):
            return str(self.num) == other
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, PageOrder):
            # TODO: Test this
            return (self.num in other.after) or (self.num not in other.before)
        elif isinstance(other, int):
            return self.num > other
        elif isinstance(other, str):
            return str(self.num) > other
        else:
            return NotImplemented


class Day5(Day):
    def get_input(self):
        page_orders: list[PageOrder] = []

        for line in super().get_input():
            try:
                before, after = [int(_) for _ in line.split('|')]
                Day5.add_page_orders(before, after, page_orders)
            except ValueError:
                break
        
        print(page_orders)

    @staticmethod
    def add_page_orders(before: int, after: int, page_orders: list[PageOrder]):
        Day5.add_one_page(before, after, page_orders, before_mode=True)
        Day5.add_one_page(after, before, page_orders, before_mode=False)
        
    @staticmethod
    def add_one_page(
        page_a: int,
        page_b: int,
        page_orders: list[PageOrder],
        before_mode: bool=True
    ):
        page_i: int = page_orders.index(page_a)
        print(page_i)

        if page_i == -1:
            page = PageOrder(page_a)
            page_orders.append(page)
        else:
            page = page_orders[page_i]

        page_list = page.before if before_mode else page.after
        page_list.append(page_b)

    def part_1(self):
        # test = [LinkedListNode(1)]
        # print(2 in test)

        self.get_input()

    def part_2(self):
        pass
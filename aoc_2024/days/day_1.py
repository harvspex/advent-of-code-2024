from aoc_2024.day_class.day import Day

class Day1(Day):
    def part_1(self):
        list_a, list_b = self.get_input()
        list_a.sort()
        list_b.sort()

        sum: int = 0

        while len(list_a) > 0:
            sum += abs(list_a.pop() - list_b.pop())

        return sum


    def part_2(self):
        list_a, list_b = self.get_input()
        sum: int = 0

        for item_a in list_a:
            sum += item_a * list_b.count(item_a)

        return sum


    def get_input(self):
        list_a, list_b = [], []

        for line in super().get_input():
            token_a, token_b = line.split()
            list_a.append(int(token_a))
            list_b.append(int(token_b))

        return list_a, list_b

from aoc_2024.day_class.day import Day

class Day3(Day):
    def part_1(self):
        instructions: str = self.get_input()
        MUL_START: str = 'mul('
        MUL_END: str = ')'
        total: int = 0
        start: int = 0
        is_processing: bool = True

        while is_processing:
            start = instructions.find(MUL_START, start)
            if start == -1:
                break
            start += len(MUL_START)

            end: int = instructions.find(MUL_END, start)
            if end == -1:
                break

            ints = Day3.parse_ints(instructions[start:end])

            if ints:
                subtotal: int = 1
                for num in ints:
                    subtotal *= num

                total += subtotal

        return total


    def part_2(self):
        instructions: str = self.get_input()
        DO: str = 'do()'
        DONT: str = 'don\'t()'
        MUL_START: str = 'mul('
        MUL_END: str = ')'
        start: int = 0

        while True:
            next_match = Day3.find_next(instructions, start, DO, DONT, MUL_START)

            if next_match is None:
                break

            index, string = next_match

            if string == DO:
                find_next_args = [DONT, MUL_START]
            elif string == DONT:
                find_next_args = [DO]
            elif string == MUL_START:
                find_next_args = [DO, DONT, MUL_START, MUL_END]
            elif string == MUL_END:
                find_next_args = [DO, DONT, MUL_START, MUL_END]


    @staticmethod
    def parse_ints(substring: str) -> list[int]:
        try:
            ints: list[int] = [int(_) for _ in substring.split(',')]
            return ints if (len(ints) == 2) else []
        except ValueError:
            return []


    @staticmethod
    def find_next(string: str, start: int, *args: str):
        next_indices = {}

        for arg in args:
            next_index = string.find(arg, start)

            if next_index != -1:
                next_indices[next_index] = arg

        sorted_indices = sorted(next_indices.items())

        return sorted_indices[0] if len(sorted_indices) > 0 else None


    def get_input(self):
        return ''.join(line.strip() for line in super().get_input())
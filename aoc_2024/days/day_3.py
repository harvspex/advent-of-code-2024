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

    @staticmethod
    def parse_ints(substring: str) -> list[int]:
        try:
            ints: list[int] = [int(_) for _ in substring.split(',')]
            return ints if (len(ints) == 2) else []
        except ValueError:
            return []

    def part_2(self):
        return

    def get_input(self):
        return ''.join(line.strip() for line in super().get_input())
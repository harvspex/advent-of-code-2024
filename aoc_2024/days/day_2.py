from aoc_2024.day_class.day import Day

class Day2(Day):
    def part_1(self):
        return self.get_safe_reports(remove_mode=False)

    def part_2(self):
        # 450 too low
        # 458 too low
        return self.get_safe_reports(remove_mode=True)

    def get_safe_reports(self, remove_mode: bool=False):
        total_safe_reports: int =0

        for report in self.get_input():
            if self.check_gradient(report, remove_mode=remove_mode):
                total_safe_reports += 1

        return total_safe_reports

    @staticmethod
    def check_gradient(
        report: list[int],
        min_g: int=1,
        max_g: int=3,
        remove_mode: bool=False
    ):
        is_safe: bool = True
        is_increasing: bool = None

        for i in range(len(report) - 1):
            # Get gradient of 2 contiguous list items
            current_g: int = report[i] - report[i+1]

            # Gradient cannot be 0
            if current_g == 0:
                is_safe = False
            # Set increasing or decreasing
            elif is_increasing is None:
                is_increasing = current_g > 0
            # Check if change in gradient direction
            elif (current_g > 0) != is_increasing:
                is_safe = False

            # Check if absolute value of gradient is within allowed limits
            if not (min_g <= abs(current_g) <= max_g):
                is_safe = False

            if not is_safe:
                break

        if remove_mode and not is_safe:
            return (
                Day2.check_gradient(Day2.remove_element(report, i), min_g, max_g, remove_mode=False)
                or Day2.check_gradient(Day2.remove_element(report, i+1), min_g, max_g, remove_mode=False)
            )
        else:
            return is_safe

    @staticmethod
    def remove_element(lst: list, i: int):
        return lst[:i] + lst[i+1:]

    def get_input(self):
        for line in super().get_input():
            yield [int(_) for _ in line.strip().split()]
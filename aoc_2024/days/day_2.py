from aoc_2024.day_class.day import Day

class Day2(Day):
    def part_1(self):
        total_safe_reports: int =0

        for report in self.get_input():
            if self.check_gradient(report):
                total_safe_reports += 1

        return total_safe_reports

    @staticmethod
    def check_gradient(report: list[int], min_g: int=1, max_g: int=3):
        is_increasing: bool=None

        for i in range(len(report) - 1):
            # Get difference of s 2 contiguous list items
            current_g: int = report[i] - report[i+1]

            # Determine if increasing or decreasing
            if (is_increasing is None) and (current_g != 0):
                is_increasing = current_g > 0
            # Return false if change in gradient direction
            elif (current_g > 0) != is_increasing:
                return False

            # Check if absolute value of gradient is within allowed limits
            if not (min_g <= abs(current_g) <= max_g):
                return False

        # All gradients within allowed limits
        return True

    def part_2(self):
        return None

    def get_input(self):
        for line in super().get_input():
            yield [int(_) for _ in line.strip().split()]
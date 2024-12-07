from aoc_2024.day_class.day import Day

class Day4(Day):
    target: str = 'XMAS'
    r_target: str = ''.join(reversed(target))
    target_len: int = len(target)
    crossword: list[list[str]] = []
    row_len: int = None
    col_len: int = None

    def part_1(self):
        self.get_input()
        return self.check_all()

    def check_all(self):
        total: int = 0
        for row_i in range(self.row_len):
            # Check all rows
            row = self.crossword[row_i]
            total += self.check_row(row)

            # If There is room below the row for a diagonal target word
            if row_i > (self.col_len - self.target_len):
                # Check all diagonals
                total += self.check_backslash(row_i)
                total += self.check_forwardslash(row_i)

        # Check all cols
        for col_i in range(self.col_len):
            self.check_column(col_i)

        return total

    def has_target(self, substring: str):
        return substring == self.target or substring == self.r_target

    def check_row(self, row: list[str]):
        total: int = 0

        for i in range(self.row_len - self.target_len):
            substring: str = ''.join(row[i : i + self.target_len])

            if self.has_target(substring):
                total += 1

        return total

    def check_column(self, col_i: int):
        column: list = [row[col_i] for row in self.crossword]
        return self.check_row(column)

    def check_backslash(self, row_i: int):
        total: int = 0

        for _ in range(self.row_len - self.target_len):
            substring: str = ''
            for char in range(self.target_len):
                substring += self.crossword[row_i + char][char]

            if self.has_target(substring):
                total += 1

        return total

    def check_forwardslash(self, row_i: int):
        total: int = 0

        for x in reversed(range(self.target_len - 1, self.row_len)):
            substring: str = ''
            for char in range(self.target_len):
                substring += self.crossword[row_i + char][x - char]

            if self.has_target(substring):
                total += 1

        return total

    def part_2(self):
        pass

    def get_input(self):
        for line in super().get_input():
            row = [ch for ch in line.strip()]
            if row:
                self.crossword.append(row)
            if self.row_len is None:
                self.row_len = len(row)
            elif self.row_len != len(row):
                raise ValueError('Error: row lengths do not match')

        self.col_len = len(self.crossword)
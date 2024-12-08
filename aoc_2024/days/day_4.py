from aoc_2024.day_class.day import Day

class Day4(Day):
    target: str = 'XMAS'
    r_target: str = ''.join(reversed(target))
    target_len: int = len(target)
    crossword: list[list[str]] = []
    num_cols: int = None
    num_rows: int = None

    def part_1(self):
        self.get_input()
        return self.check_all()

    def check_all(self):
        total: int = 0

        for row_i in range(self.num_rows):

            # Check all rows
            row = self.crossword[row_i]
            total += self.check_row(row)

            # If There is room below the current row for a diagonal target word
            if row_i < (self.num_rows - (self.target_len - 1)):

                # Check all diagonals
                total += self.check_diagonal(row_i)
                total += self.check_diagonal(row_i, reverse=True)

        # Check all columns
        for col_i in range(self.num_cols):
            total += self.check_column(col_i)

        return total

    def has_target(self, substring: str):
        return substring == self.target or substring == self.r_target

    def check_row(self, row: list[str]):
        total: int = 0

        for i in range(self.num_cols - (self.target_len-1)):
            substring: str = ''.join(row[i : i + self.target_len])

            if self.has_target(substring):
                total += 1

        return total

    def check_column(self, col_i: int):
        column: list = [row[col_i] for row in self.crossword]
        return self.check_row(column)

    def check_diagonal(self, row_i: int, reverse: bool=False):
        total: int = 0

        row_range = range(self.num_cols - (self.target_len-1))
        get_char = lambda char: char
        
        if reverse:
            row_range = reversed(range(self.target_len-1, self.num_cols))
            get_char = lambda char: -char
        
        for x in row_range:
            substring: str = ''

            for char in range(self.target_len):
                next_row_down = self.crossword[row_i + char]
                next_diagonal_char = next_row_down[x + get_char(char)]
                substring += next_diagonal_char

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
            if self.num_cols is None:
                self.num_cols = len(row)
            elif self.num_cols != len(row):
                raise ValueError('Error: row lengths do not match')

        self.num_rows = len(self.crossword)

        print(f'num rows: {self.num_rows}')
        print(f'num cols: {self.num_cols}')
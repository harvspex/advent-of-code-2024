from aoc_2024.day_class.day import Day

class Day4(Day):
    target: str = 'XMAS'
    r_target: str = ''.join(reversed(target))
    target_len: int = len(target)
    crossword: list[list[str]] = []
    num_cols: int = None
    num_rows: int = None

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
        self.get_input()
        target = 'MAS'

    def yield_intersections(self, target: str):
        len_target = len(target)
        if len_target % 2 == 0:
            raise ValueError('Target word cannot have even number of letters.')

        middle_index: int = len_target // 2
        middle_letter: str = target[middle_index]
        remainder: int = len(target[:middle_index])

        for row_i in range(remainder, self.num_rows-remainder):
            for col_i in range(remainder, self.num_cols-remainder):
                if self.crossword[row_i][col_i] == middle_letter:
                    yield (row_i, col_i)

    def check_for_mas(self, coords: tuple[int, int], target='MAS'):
        # Checks 4 diagonal coordinates surrounding the provided coords tuple.
        # Inflexible = only works for target of length 3
        # Could be improved
        r_target = ''.join(reversed(target))
        
        self.get_mas_substring(coords) 

    def get_mas_substring(self, coords: tuple[int, int], reverse: bool=False):
        coords_shifts = [(1,1),(0,0),(-1,-1)] if reverse else [(-1,1),(0,0),(1,-1)]

        substring = ''
        x, y = coords

        for x_shift, y_shift in coords_shifts:
            substring += self.crossword[x+x_shift][y+y_shift]

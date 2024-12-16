
import numpy as np
import re
from typing import List


class SolutionDay4:

    def __init__(self, filename):
        with open(filename) as file:
            self.data = [line.strip('\n') for line in file.readlines()]
        self.counter = 0
        self.pattern = r"XMAS|SAMX"
        self.word = 'MAS'
        self.reversed_word = ''.join(self.word[::-1])
        self.part2_search = {'M', 'S'}

    def part1(self):
        lines = self.data[:]
        # converts each row to item in list
        lines.extend(["".join([row[i] for row in self.data])
                     for i in range(len(self.data[0]))])
        main_diagnols, anti_diagnols = self.find_diagnols(self.data)
        lines.extend([''.join(i) for i in main_diagnols.values()])
        lines.extend([''.join(i) for i in anti_diagnols.values()])
        return sum(line.count(self.word) + line.count(self.reversed_word) for line in lines)

    def parse_regex(self, pattern) -> List[str]:
        matches = re.findall(pattern, self.data)
        return matches

    def find_diagnols(self, grid):
        rows, cols = len(grid), len(grid[0])

        # from top-left to bottom-right
        main_diagonals = {}

        # from top-right to bottom-left
        anti_diagonals = {}

        for r in range(rows):
            for c in range(cols):
                key_main = r - c
                if key_main not in main_diagonals:
                    main_diagonals[key_main] = []
                main_diagonals[key_main].append(grid[r][c])

                key_anti = r + c
                if key_anti not in anti_diagonals:
                    anti_diagonals[key_anti] = []
                anti_diagonals[key_anti].append(grid[r][c])

        return main_diagonals, anti_diagonals

    def part2(self):
        """
            Take in 2d Matrix: loop through rows and columns
            each time we come across an X we check the diagnols
            i.e. grid[i][j] == "X" we check the following
            - above and left: grid[i-1][j-1]
            - above and right: grid[i-1][j+1]
            - below and left: grid[i+1][j-1]
            - below and right: grid[i+1][j+1]
        - for each of these we check if they are grid[i-1][j-1], grid[i-1][j+1] in {'M', 'S'}
        """
        grid = self.data
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(1, rows-1):  # avoid index out of bounds errors
            for j in range(1, cols-1):
                if grid[i][j] == 'A':
                    # above and left and below and right, above and right wth below and left makes a cross
                    if {grid[i-1][j-1], grid[i+1][j+1]} == self.part2_search and {grid[i-1][j+1], grid[i+1][j-1]} == self.part2_search:
                        count += 1
        return count

    def main(self):
        part1_res = self.part1()
        part2_res = self.part2()
        return part1_res, part2_res


if __name__ == "__main__":
    filename = 'day4/day4.txt'
    sol = SolutionDay4(filename)
    part1_result, part2_result = sol.main()
    print(part1_result, part2_result)

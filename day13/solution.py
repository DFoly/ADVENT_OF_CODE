import argparse
from typing import List, Set, Tuple
import os
import sys
import numpy as np
import re
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))


class Solution:

    def __init__(self):
        pass

    def parse_equations(self):
        digits = [re.findall(r'\d+', val[0]) for val in self.data]
        digits = [[int(element) for element in sublist]
                  for sublist in digits]
        new_list = []
        for i in range(0, len(digits), 4):  # Step by 4
            new_list.append(digits[i:i+3])
        return new_list

    def solve_equation(self, instructions: list, adjustment: int = 0):
        """
            Pass in 2d array
            First two lists should be stacked
            equation: [a1 b1]
                      [a2 b2]
            y = [y1]
                [y2]
        """
        A = np.array((instructions[0]))
        B = np.array((instructions[1]))
        array = np.stack((A, B), axis=1)
        y = np.array(instructions[2]) + adjustment
        ans = np.rint(np.linalg.solve(array, y))
        answer_check = array @ ans
        return (ans, answer_check == y)

    def part1(self):
        total = 0
        self.data = self.parse_equations()

        for i in range(0, len(self.data)):
            ans_array, answer_check = self.solve_equation(self.data[i])
            A, B = ans_array
            if int(A) == A and int(B) == B and np.all(answer_check):
                total += A*3 + B*1
        return total

    def part2(self):
        """

        """
        ADJUSTMENT = 10_000_000_000_000
        total = 0
        for i in range(0, len(self.data)):
            ans_array, answer_check = self.solve_equation(
                self.data[i], adjustment=ADJUSTMENT)
            A, B = ans_array
            if int(A) == A and int(B) == B and np.all(answer_check):
                total += A*3 + B*1
        return total

    def main(self):
        with open(sys.argv[1]) as f:
            self.data = []
            for line in f.readlines():
                self.data.append(line.strip().split('\n\n'))

        # print(self.data)
        # Solve parts
        print("Part 1:", self.part1())
        print("Part 2:", self.part2())


if __name__ == "__main__":
    sol = Solution()
    sol.main()

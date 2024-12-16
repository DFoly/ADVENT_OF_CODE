import re
import numpy as np
from typing import List


class SolutionDay3:

    def __init__(self, filename):
        with open(filename) as file:
            self.data = file.read()
        self.valid_regex = r"mul\([0-9]+,[0-9]+\)"
        self.valid_regex_part2 = r"mul\([0-9]+,[0-9]+\)|don't\(\)|do\(\)"
        self.digit_regex = r"\d+"
        self.total_sum_part1 = 0
        self.total_sum_part2 = 0

    def parse_regex(self, pattern) -> List[str]:
        matches = re.findall(pattern, self.data)
        return matches

    def find_digits(self, matches: List[str]):
        for i in matches:
            digits = re.findall(self.digit_regex, i)
            product = np.prod([int(i) for i in digits])
            self.total_sum_part1 += product
        return digits

    def find_digits_part2(self, matches: List[str]):
        prev = "do()"
        for i in matches:
            if i == "don't()" or (prev == "don't()" and i != "do()"):
                prev = "don't()"
                continue
            if i == "do()":  # dont want to process and empty array which returns 1
                prev = "do()"
                continue
            if (prev == "do()" and i != "don't()"):

                digits = re.findall(self.digit_regex, i)
                product = np.prod([int(i) for i in digits])
                self.total_sum_part2 += int(product)
        return digits

    def part1(self):
        matches = self.parse_regex(self.valid_regex)
        digits = self.find_digits(matches)
        return self.total_sum_part1

    def part2(self):
        matches = self.parse_regex(self.valid_regex_part2)
        digits = self.find_digits_part2(matches)
        return self.total_sum_part2

    def main(self):
        part1_res = self.part1()
        part2_res = self.part2()
        return part1_res, part2_res


if __name__ == "__main__":
    filename = 'day3/day3.txt'
    sol = SolutionDay3(filename)
    part1_result, part2_result = sol.main()
    print(part1_result, part2_result)

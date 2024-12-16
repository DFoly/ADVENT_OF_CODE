from typing import List, Set, Tuple


class Solution:

    def __init__(self, filename):
        with open(filename) as f:
            self.data = [line.split(':') for line in f.readlines()]

    def part1(self):
        count = 0
        for target, numbers in self.hash_map.items():
            count += self.calculate_equation(numbers,
                                             target, operations=self.operators)
        return count

    def part2(self):
        pass

    def main(self):
        part1 = self.part1()
        part2 = self.part2()
        return part1, part2


if __name__ == "__main__":
    filename = 'day7/day7.txt'
    solution = Solution(filename)
    part1, part2 = solution.main()
    print(part1, part2)

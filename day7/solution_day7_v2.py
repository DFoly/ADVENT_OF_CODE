from typing import List, Set, Tuple
import operator
from itertools import product


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def concatenate(a: int, b: int) -> int:
    pass


class Solution:

    def __init__(self, filename):
        with open(filename) as f:
            self.data = [line.split(':') for line in f.readlines()]
            self.hash_map = dict()
            for i in self.data:
                # store in reverse order so we can pop off the stack
                self.hash_map[int(i[0])] = i[1].strip().split(' ')
            for key, vals in self.hash_map.items():
                self.hash_map[key] = [int(i) for i in vals]
            print(self.hash_map)
            self.operators = [add, multiply]

    def part1_alt(self):
        """
            Brute force: take first number and add an multiplt
            by all others in the array and store results
            After we do this we check if the target is in the array
        """
        equations = []
        for line in self.data:
            test_value, numbers = line[0], line[1]
            equations.append(
                (int(test_value), [*map(int, numbers.strip().split())]))

        result = []

        for test_value, numbers in equations:
            possibles = [numbers.pop(0)]
            while numbers:
                curr = numbers.pop(0)
                temp = []
                for p in possibles:
                    temp.append(p + curr)
                    temp.append(p * curr)
                possibles = temp

            if test_value in possibles:
                result.append(test_value)

        return sum(result)

    def part2_alt(self):
        """
            Brute force: take first number and add an multiplt
            by all others in the array and store results
            After we do this we check if the target is in the array
        """
        equations = []
        for line in self.data:
            test_value, numbers = line[0], line[1]
            equations.append(
                (int(test_value), [*map(int, numbers.strip().split())]))

        result = []

        for test_value, numbers in equations:
            # keep track of previous results and add * and || the new number
            possibles = [numbers.pop(0)]
            while numbers:
                curr = numbers.pop(0)
                temp = []
                for p in possibles:
                    temp.append(p + curr)
                    temp.append(p * curr)
                    temp.append(int(f'{p}{curr}'))
                possibles = temp

            if test_value in possibles:
                result.append(test_value)

        return sum(result)

    def calculate_equation(self, numbers, target, operations):
        """
        """
        combinations = list(product(operations, repeat=len(numbers)-1))
        result = 0
        for combination in combinations:
            for i, operation in enumerate(combination):
                if i == 0:
                    result = operation(numbers[i], numbers[i+1])
                else:
                    result = operation(result, numbers[i+1])
            if result == target:
                return target
        return 0

    def part1(self):
        count = 0
        for target, numbers in self.hash_map.items():
            count += self.calculate_equation(numbers,
                                             target, operations=self.operators)
        return count

    def part2(self):
        pass

    def main(self):
        part1 = self.part1_alt()
        part2 = self.part2_alt()
        return part1, part2


if __name__ == "__main__":
    filename = 'day7/day7.txt'
    solution = Solution(filename)
    part1, part2 = solution.main()
    print(part1, part2)

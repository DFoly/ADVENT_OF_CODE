from typing import List, Set, Tuple
import operator
from itertools import product


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
            self.operators = ['+', '*']

    def part1_alt(self):
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

    def is_match(self, target, numbers):
        """
            Use product to create all combinations
            of operators with numbers
            and then iteratively build an equation and check result.
        """
        num_operators = len(numbers) - 1
        combinations = product(self.operators, repeat=num_operators)
        for combination in combinations:
            result = numbers[0]
            for i, operator in enumerate(combination):
                if operator == '+':
                    result += numbers[i+1]
                elif operator == '*':
                    result *= numbers[i+1]
            if result > target:
                continue
            elif result == target:
                return True
        return False

    def check_equation(self, target: int, nums: List[int]) -> bool:
        """
        Recursive solution:
        work backwards and we check numbers
        divides evenly into target: if not then answer wont
        work. essentially we do the reverse of * and + to figure
        out if it works
        """
        if len(nums) == 1:
            return target == nums[0]
        num = nums.pop()
        # if division
        if target % num == 0:
            if self.check_equation(target // num, nums):
                return True
        if target - num >= 0:
            if self.check_equation(target - num, nums):
                return True
        return False

    def part1_recurse(self):
        count = 0
        results = []
        for target, numbers in self.hash_map.items():
            match_flag = self.check_equation(target, numbers)
            if match_flag:
                count += target
            results.append(match_flag)
        return results, count

    def part1_combo(self):
        count = 0
        results = []
        for target, numbers in self.hash_map.items():
            match_flag = self.is_match(target, numbers)
            if match_flag:
                count += target
            results.append(match_flag)
        return results, count

    def testing(self):
        combos, count = self.part1_combo()
        recurse, count = self.part1_recurse()
        counter = 0
        results = dict()
        for c, r in zip(combos, recurse):
            if c != r:
                results[counter] = (c, r)
            counter += 1
        return results

    def part2(self):
        pass

    def main(self):
        part1, count = self.part1_recurse()
        count2 = self.part1_alt()
        # part2 = self.part2()
        # return part1, part2
        return part1, count, count2


if __name__ == "__main__":
    filename = 'day7/day7_test.txt'
    solution = Solution(filename)
    part1, count, count2 = solution.main()
    print(solution.testing())
    print(count2)


# [False, True, False, False, False, False, False, False, True, False, False, True, False, True, False, True]: CHECK_equation
# [False, True, False, False, False, False, True, False, True, False, False, True, False, True, False, True]: is_match

# 12839601725776
# 8612094229224

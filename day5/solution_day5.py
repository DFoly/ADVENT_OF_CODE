
from collections import defaultdict
import numpy as np
import re
from typing import List
import random


class SolutionDay4:
    def __init__(self, filename):
        with open(filename) as file:
            self.data = [line.strip('\n') for line in file.readlines()]
            self.split_index = self.data.index('')
            self.page_rules, self.page_updates = self.data[:
                                                           self.split_index], self.data[self.split_index + 1:]
            self.page_rules_dict = self.parse_rules()
            print(self.page_rules_dict)

    def parse_rules(self) -> dict:
        """
        Store rules in dictionary
        Key is left page and use List to append right pages
        under the same key in order
        """
        page_rules_dict = defaultdict(set)
        for i in self.page_rules:
            key, value = i.split('|')
            page_rules_dict[key].add(value)
        return page_rules_dict

    def is_valid(self, line_array: List[str]) -> bool:
        """
            Valid def: {'75', '47', '61', '53', '29'}
            - if each number following i is contained in the rules page
              for key i then the rule works: if not we return False
        """
        for i in range(len(line_array)):
            for j in range(i+1, len(line_array)):
                if str(line_array[j]) not in self.page_rules_dict[line_array[i]]:
                    return False
        return True


    def fix_bad_updates(self, line: str) -> int:
        """
            Takes in lines that are bad and reorders them
            so they obey the rules.
        """
        line_array = [int(i) for i in line.split(',')]
        flag = False
        nums = 0
        seen = set()
        while not flag:
            nums += 1
            np.random.shuffle(line_array)  # inplace
            if tuple(line_array) in seen:
                continue
            else:
                seen.add(tuple(line_array))
            result = self.is_valid(line_array)
            if result:
                flag = True
                return line_array[len(line_array) // 2]
            if nums % 100 == 0:
                print('num iters: ', nums)

    def part1(self):
        # get updates
        results = []
        count = 0
        bad_values_count = 0
        for line in self.page_updates:
            line_array = [i for i in line.split(',')]
            ans = self.is_valid(line_array)
            if ans:
                results.append(ans)
                line_array = [int(i) for i in line.split(',')]
                count += line_array[len(line_array) // 2]  # add middle value
            else:
                print(line)
                # fix bad values
                bad_values_count += self.fix_bad_updates(line)
        return count, bad_values_count

    def part2(self):
        pass

    def main(self):
        part1_res = self.part1()
        #part2_res = self.part2()
        return part1_res,  # part2_res


if __name__ == "__main__":
    filename = 'day5/day5_test.txt'
    sol = SolutionDay4(filename)
    part1_result, part2_result = sol.main()
    print(part1_result, part2_result)

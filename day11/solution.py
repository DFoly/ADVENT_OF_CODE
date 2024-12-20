import argparse
from typing import List, Set, Tuple, Union
import os
from collections import Counter, defaultdict

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))


class Solution:

    def __init__(self):
        pass

    def apply_rule(self, data: list) -> list:
        """
            Brute forces using lists
        """
        new_data = []
        for value in data:
            if value == 0:
                new_data.append(1)
            else:
                value_str = str(value)
                if len(value_str) % 2 == 0:
                    new_data.extend(self.even_split_stones(value_str))
                else:
                    new_data.append(value * 2024)
        return new_data

    def apply_rule_optimized(self, data_counter: Counter) -> Counter:
        """ Use hashmap for much greater efficiency
            We store the numbers as key and the count as values
        """
        new_counter = Counter()
        for value, count in data_counter.items():
            if value == 0:
                new_counter[1] += count  # Convert all 0s to 1s
            else:
                value_str = str(value)
                if len(value_str) % 2 == 0:
                    # Split evenly
                    half1, half2 = self.even_split_stones(value_str)
                    new_counter[half1] += count
                    new_counter[half2] += count
                else:
                    # Multiply by 2024
                    new_value = value * 2024
                    new_counter[new_value] += count
        return new_counter

    def even_split_stones(self, curr_value: str) -> Tuple[int, int]:
        """Split stones in half."""
        mid_point = len(curr_value) // 2
        return int(curr_value[:mid_point]), int(curr_value[mid_point:])

    def part1(self, blinks: int) -> int:
        data = self.data[:]
        for i in range(blinks):
            data = self.apply_rule(data)
            print('Finished Iteration: ', i)
        return len(data)

    def part2(self, blinks: int) -> int:
        # Hashmap: store each computed number as a key and count as value
        # much more salable
        # Initialize the frequency map with the initial data
        data_counter = Counter(self.data)
        print(data_counter)

        for i in range(blinks):
            data_counter = self.apply_rule_optimized(data_counter)
            print(
                f'Finished Iteration {i}, Total Stones: {sum(data_counter.values())}')

        return sum(data_counter.values())

    def main(self):
        # Parse command-line arguments
        parser = argparse.ArgumentParser(description="Advent of Code Day 11")
        parser.add_argument('--t', action='store_true',
                            help="Use test input instead of main input")
        args = parser.parse_args()

        # Select input file
        filename = "test.txt" if args.t else "input.txt"
        # Construct paths relative to the script directory
        self.filename = os.path.join(script_dir, filename)
        with open(self.filename) as f:
            self.data = [line.split(' ') for line in f.readlines()][0]
            self.data = [int(i) for i in self.data]

        # print(self.data)
        # Solve parts
        blinks = 75
        #print("Part 1:", self.part1(blinks))
        print("Part 2:", self.part2(blinks))


if __name__ == "__main__":
    sol = Solution()
    sol.main()

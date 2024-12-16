import argparse
from typing import List

from typing import List, Set, Tuple
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))


class Solution:

    def __init__(self):
        pass

    def part1(self):
        pass

    def part2(self):
        pass

    def main(self):
        # Parse command-line arguments
        parser = argparse.ArgumentParser(description="Advent of Code Day 9")
        parser.add_argument('--t', action='store_true', help="Use test input instead of main input")
        args = parser.parse_args()
        
        # Select input file
        filename = "test.txt" if args.t else "input.txt"
        # Construct paths relative to the script directory
        self.filename = os.path.join(script_dir, filename)
        with open(self.filename) as f:
            self.data = [line.split(':') for line in f.readlines()]

        print(self.data)
        # Solve parts
        print("Part 1:", self.part1())
        print("Part 2:", self.part2())

if __name__ == "__main__":
    sol = Solution()
    sol.main()

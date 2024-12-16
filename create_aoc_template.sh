#!/bin/bash

# Check if a day number is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <day_number>"
  exit 1
fi

# Pad the day number to 2 digits (e.g., 1 -> 01, 10 -> 10)
DAY=$(printf "day%02d" "$1")

# Create the folder for the day
mkdir -p "$DAY"

# Navigate into the folder
cd "$DAY" || exit

# Create Python solution file
cat > solution.py <<EOF
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
        parser = argparse.ArgumentParser(description="Advent of Code Day $1")
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
EOF

# Create empty input and test files
touch input.txt test.txt

# Optionally create a README for the day's problem
cat > README.md <<EOF
# Advent of Code - Day $1

## Problem Description

Paste the problem description here.

## Running the Solution

### Using Main Input:
\`\`\`bash
python solution.py
\`\`\`

### Using Test Input:
\`\`\`bash
python solution.py --test
\`\`\`
EOF

echo "Template for $DAY created successfully!"
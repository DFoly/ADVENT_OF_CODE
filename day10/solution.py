import argparse
from typing import List

from typing import List, Set, Tuple
import os
from collections import deque

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))


class Solution:

    def __init__(self):
        pass

    def find_trail_heads(self):
        trail_head_locations = []
        n_rows, n_cols = range(len(self.grid)), range(len(self.grid[0]))
        for row in n_rows:
            for col in n_cols:
                if self.grid[row][col] == 0:
                    trail_head_locations.append((row, col))
        return trail_head_locations

    def part1_bfs(self):
        """ BFS using deque: For each trial start: 0 we count
            the number of distinct trial end points 9's it can reach.
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        n_rows, n_cols = len(self.grid), len(self.grid[0])

        def bfs(row, col):
            trail_ends = set()
            queue = deque([(row, col)])
            while queue:
                # print(queue)
                row, col = queue.popleft()
                # print(queue)
                if self.grid[row][col] == 9:
                    trail_ends.add((row, col))
                    continue
                for dr, dc in directions:
                    new_row, new_col = row + dr,  col + dc
                    if 0 <= new_row < n_rows and 0 <= new_col < n_cols and self.grid[row][col] + 1 == self.grid[new_row][new_col]:
                        queue.append((new_row, new_col))
                        # print(queue)
            return len(trail_ends)

        # Find all trail heads (cells with value 0)
        trail_head_locations = self.find_trail_heads()
        ans = 0
        for location in trail_head_locations:
            ans += bfs(*location)
        return ans

    def part2_bfs(self):
        """
            Now we want to count all unique paths to trial end
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        n_rows, n_cols = len(self.grid), len(self.grid[0])

        trail_ends = set()

        def bfs(row, col):
            queue = deque([(row, col)])
            path_count = 0
            while len(queue) > 0:
                row, col = queue.popleft()

                if self.grid[row][col] == 9:
                    path_count += 1
                    trail_ends.add((row, col))
                    continue

                for dr, dc in directions:
                    new_row, new_col = row + dr,  col + dc
                    if 0 <= new_row < n_rows and 0 <= new_col < n_cols and self.grid[row][col] + 1 == self.grid[new_row][new_col]:
                        queue.append((new_row, new_col))
            return path_count

        trail_head_locations = self.find_trail_heads()
        total_paths = 0
        for location in trail_head_locations:
            total_paths += bfs(*location)
        return total_paths

    def part1_dfs(self):
        """ 
        DFS using recursion to count all unique 9 cells reachable from 0 cells.
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        n_rows, n_cols = len(self.grid), len(self.grid[0])
        # To store unique trail ends (cells with value 9)
        visited = set()
        targets = 0

        def dfs(row, col, current_value):
            # Base cases: out of bounds or incorrect value
            nonlocal targets
            visited.add((row, col))
            # If we reach 9, add the cell to the visited set and stop
            if self.grid[row][col] == 9:
                targets += 1

            # if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
            #     return
            # if self.grid[row][col] != current_value:
            #     return
            # if (row, col) in visited:
            #     return
            # Explore all directions recursively
            for dr, dc in directions:
                if row < 0 or row >= n_rows or col < 0 or col >= n_cols \
                        and self.grid[row][col] != current_value \
                        and (row, col) not in visited:
                    dfs(row + dr, col + dc, current_value + 1)

        # Find all trail heads (cells with value 0)
        trail_head_locations = self.find_trail_heads()

        # Start DFS from each trail head
        for row, col in trail_head_locations:
            dfs(row, col, 0)  # Start DFS with value 0

        # Return the number of unique trail ends
        return targets  # len(visited)

    def part2_dfs(self):
        """ 
        DFS using recursion to count all distinct trails which begin
        at specific trail head.
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        n_rows, n_cols = len(self.grid), len(self.grid[0])
        visited = set()

        def dfs(row, col, current_value):
            # Base cases: out of bounds or incorrect value
            if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
                return 0
            if self.grid[row][col] != current_value:
                return 0

            # If we reach 9, count this trail end
            if self.grid[row][col] == 9 and self.grid[row][col] not in visited:
                visited.add((row, col))
                return 1

            # Explore all directions and accumulate the count of trails
            trail_count = 0
            for dr, dc in directions:
                trail_count += dfs(row + dr, col + dc, current_value + 1)

            return trail_count

        # Find all trail heads (cells with value 0)
        trail_head_locations = self.find_trail_heads()
        total_trails = 0

        # Start DFS from each trail head
        for row, col in trail_head_locations:
            total_trails += dfs(row, col, 0)  # Start DFS with value 0

        return total_trails

    def main(self):
        # Parse command-line arguments
        parser = argparse.ArgumentParser(description="Advent of Code Day 10")
        parser.add_argument('--t', action='store_true',
                            help="Use test input instead of main input")
        args = parser.parse_args()

        # Select input file
        filename = "test.txt" if args.t else "input.txt"
        # Construct paths relative to the script directory
        self.filename = os.path.join(script_dir, filename)
        with open(self.filename) as f:
            self.data = [line.strip().split('\n') for line in f.readlines()]
            self.grid = [[int(char) for char in item]
                         for sublist in self.data for item in sublist]

        # print(self.grid)
        # Solve parts
        print("Part 1 BFS:", self.part1_bfs())
        print("Part 2 BFS:", self.part2_bfs())
        print("Part 1 DFS:", self.part1_dfs())
        print("Part 2 DFS:", self.part2_dfs())


if __name__ == "__main__":
    sol = Solution()
    sol.main()

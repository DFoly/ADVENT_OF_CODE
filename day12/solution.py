import argparse
from typing import List, Set, Tuple
from collections import defaultdict, deque
import os
import sys

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))


class Solution:

    def __init__(self):
        pass

    def sides(self, region: set[tuple[int]]):
        """
            Goal is to count the corners of the region:
            For a square region we should have 4 corners, i.e. 4 sides.
            We take in each region: connected plots
            For each row, col we check direct neigbour points:
            for example: for every direction if the cell is not in region
            then we are at the edge of the region
        """
        up, down, left, right = (set() for _ in range(4))
        for r, c in region:
            if (r - 1, c) not in region:
                up.add((r, c))
            if (r + 1, c) not in region:
                down.add((r, c))
            if (r, c - 1) not in region:
                left.add((r, c))
            if (r, c + 1) not in region:
                right.add((r, c))

        count = 0
        for r, c in up:
            if (r, c) in left:
                count += 1
            if (r, c) in right:
                count += 1
            if (r - 1, c - 1) in right and (r, c) not in left:
                count += 1
            if (r - 1, c + 1) in left and (r, c) not in right:
                count += 1

        for r, c in down:
            if (r, c) in left:
                count += 1
            if (r, c) in right:
                count += 1
            if (r + 1, c - 1) in right and (r, c) not in left:
                count += 1
            if (r + 1, c + 1) in left and (r, c) not in right:
                count += 1

        return count

    def part1(self):
        """BFS

        """
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        num_rows, num_cols = len(self.grid), len(self.grid[0])
        connected_plots = set()

        def bfs(row, col):
            """
                base cases:
                 - if (row, col) in conected_plots: continue
                 - if grid[row][col] != plant type continue and build fence around perimeter
                 Else:
                  cell is valid so add to connected and explore 4 directions:
                   - if not visited already we add to queue
                - total value will be the len(connected) * perimeter
            """
            queue = deque([(row, col)])
            perimeter = 0
            connected_plots = set()
            plant_type = self.grid[row][col]

            while len(queue) > 0:
                row, col = queue.popleft()
                if (row, col) in connected_plots:  # dont want to search where we have already visited
                    continue

                if not (0 <= row < num_rows and 0 <= col < num_cols) or self.grid[row][col] != plant_type:
                    perimeter += 1  # biuld perimeter perimeter
                    continue

                # onyl add if the same plant type
                connected_plots.add((row, col))
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if (new_row, new_col) not in connected_plots:
                        # add all neighbours to the queue so we can visit
                        queue.append((new_row, new_col))
            return connected_plots, len(connected_plots) * perimeter

        total_cost = 0
        visited = set()  # stored all conected plants
        regions = []
        for row in range(num_rows):
            for col in range(num_cols):
                if (row, col) not in visited:
                    connected_plots, cost = bfs(row, col)
                    visited |= connected_plots
                    regions.append(connected_plots)
                    # plant_locations[self.grid[row][col]].extend(
                    #    connected_plants)
                    total_cost += cost
        return regions, visited, total_cost  # plant_locations, total_cost

    def part2(self):
        regions, visited, total_cost = self.part1()
        total = 0
        for region in regions:
            print(len(region), self.sides(region),
                  self.sides(region) * len(region))
            total += self.sides(region) * len(region)
        return total

    def main(self):
        with open(sys.argv[1]) as f:
            self.grid = []
            for line in f.readlines():
                self.grid.append(list(line.strip()))

        print(self.grid)
        # Solve parts
        print("Part 1:", self.part1())
        print("Part 2:", self.part2())


if __name__ == "__main__":
    sol = Solution()
    sol.main()

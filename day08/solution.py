import argparse
from typing import List, Set, Tuple
from collections import defaultdict
import numpy as np
from itertools import combinations


class Solution:

    def __init__(self):
        pass

    def find_locations(self):
        rows = range(len(self.grid))
        cols = range(len(self.grid[0]))
        print(rows, cols)
        hash_map = defaultdict(list)
        for row in rows:
            for col in cols:
                cell = self.grid[row][col]
                if cell != '.':
                    hash_map[cell].append((row, col))
        return hash_map

    def part1_alt(self):
        antennas = defaultdict(list)
        rows, cols = len(self.grid), len(self.grid[0])
        for row in range(rows):
            for col in range(cols):
                if self.grid[row][col] != ".":
                    antennas[self.grid[row][col]].append((row, col))
        antinodes = set()

        for antenna, coords in antennas.items():
            for i in range(len(coords)):
                for j in range(i + 1, len(coords)):
                    diff = tuple(a - b for a, b in zip(coords[j], coords[i]))
                    for _idx, _dir in [(i, -1), (j, 1)]:
                        pos = tuple(
                            [a + b * _dir for a, b in zip(coords[_idx], diff)])
                        if 0 <= pos[0] < rows and 0 <= pos[1] < cols:
                            antinodes.add(pos)
        return len(antinodes)

    def compute_antinode_locations(self, antenna: str, locations: List[Tuple[int, int]]):
        """
        """
        hash_map_new_locations = set()  # defaultdict(set)
        for (x1, y1), (x2, y2) in combinations(locations, 2):
            dx = x2-x1
            dy = y2-y1

            # add in both directions: x1-dx = x1 -(x2-x1) = 2*x1-x2
            p1 = (x1-dx, y1-dy)
            p2 = (x2+dx, y2+dy)
            # check if new points are in the grid: dont include end points
            if 0 <= p1[0] < len(self.grid) and 0 <= p1[1] < len(self.grid[0]):
                hash_map_new_locations.add(p1)
            if 0 <= p2[0] < len(self.grid) and 0 <= p2[1] < len(self.grid[0]):
                hash_map_new_locations.add(p2)
        return hash_map_new_locations

    def compute_antinode_locations_part2(self, antenna: str, locations: List[Tuple[int, int]]):
        """
            get combinaions of 2 points
            compute distance from each point
            add and substract the difference until we exhause the grid
        """
        hash_map_new_locations = set()
        for (x1, y1), (x2, y2) in combinations(locations, 2):
            dx = x2-x1
            dy = y2-y1

            # starting points
            row, col = x1, y1
            # add in both directions: x1-dx = x1 -(x2-x1) = 2*x1-x2
            # increase points: assumes starting points count
            while 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0]):
                hash_map_new_locations.add((row, col))
                row += dx
                col += dy
            row, col = x1, y1  # reset to original values
            # decrease points
            while 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0]):
                hash_map_new_locations.add((row, col))
                row -= dx
                col -= dy
        return hash_map_new_locations


    def part1(self):
        answer_set = set()
        hash_map = self.find_locations()
        for antenna, locations in hash_map.items():
            #print(antenna, locations)
            antinodes: set = self.compute_antinode_locations(
                antenna, locations)
            answer_set = answer_set.union(antinodes)
        return len(answer_set)

    def part2(self):
        """

        """
        answer_set = set()
        hash_map = self.find_locations()
        for antenna, locations in hash_map.items():
            #print(antenna, locations)
            antinodes: set = self.compute_antinode_locations_part2(
                antenna, locations)
            answer_set = answer_set.union(antinodes)
        return len(answer_set)

    def main(self):
        # Parse command-line arguments
        parser = argparse.ArgumentParser(description="Advent of Code Day 8")
        parser.add_argument('--t', action='store_true',
                            help="Use test input instead of main input")
        args = parser.parse_args()

        # Select input file
        self.filename = "test.txt" if args.t else "input.txt"
        # with open('day08/'+self.filename) as f:
        with open(self.filename) as f:
            self.grid = []
            for line in f.readlines():
                self.grid.append(list(line.strip()))

        # print(self.grid)
        # Solve parts
        print("Part 1:", self.part1())
        # print("Part 1 alt:", self.part1_alt())
        print("Part 2:", self.part2())


if __name__ == "__main__":
    sol = Solution()
    sol.main()

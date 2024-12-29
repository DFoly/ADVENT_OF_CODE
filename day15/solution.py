import argparse
from typing import List, Set, Tuple
import os
import sys
import numpy as np
from collections import deque
import copy
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))


class Solution:
    def __init__(self):
        with open(sys.argv[1]) as f:
            self.grid = []
            grid_str, moves = f.read().split("\n\n")
            self.grid = [list(row) for row in grid_str.split("\n")]
            self.moves = moves.replace("\n", "")
            self.original_grid = copy.deepcopy(self.grid)
        self.num_rows = len(self.grid)
        self.num_cols = len(self.grid[0])
        self.robot_initial_pos = self.find_robot_initial_pos()
        self.directions = {
            '^': (-1, 0),  # up
            'v': (1, 0),  # down
            '>': (0, 1),  # right
            '<': (0, -1)  # left
        }
        self.visited_q = deque(
            [(self.robot_initial_pos[0], self.robot_initial_pos[0])])
        self.visited_q_new = deque(
            [(self.robot_initial_pos[0]*2, self.robot_initial_pos[0])])

    def move_robot(self, move: str, row: int, col: int):
        """
            Robot will move unless
            blocked by a wall or hit into
            a box.
        """
        if not (0 <= row < self.num_rows and 0 <= col < self.num_cols):
            return False
        # check new position
        if self.grid[row][col] == '#':
            return False
        if self.grid[row][col] == 'O':
            return self.move_box(move, row, col)
        else:
            # updated robot position
            self.grid[row][col] = '@'
            r, c = self.visited_q.popleft()
            self.grid[r][c] = '.'
            self.visited_q.append((row, col))
            return True

    def compute_distance(self, row, col):
        """
        """
        return 100 * row + col

    def shift_boxes(self, row: int, col: int, dr: int, dc: int, value) -> set:
        """Find all contiguous boxes
           shift all the boxes
        """
        return True

    def is_valid_move(self, move: str, row: int, col: int, dr: int, dc: int) -> set:
        """
            If we hit a [ or ] we keep moving in the same
            direction until we hit a wall or a .
        """
        visited = set()
        while self.new_grid[row][col] in ['[', ']']:
            visited.add((row, col))
            new_row, new_col = row + dr, col + dc
            if self.new_grid[new_row][new_col] == '#':
                return set()
        return visited

    def move_box(self, move: str, row: int, col: int) -> bool:
        """
            Can only move a box if we are not
            bocked by a wall.
            If we are against another box we need
            to continue to check if there are boxes in
            the same direction: DFS??
            If we hit O we need to keep checking how many
            0's are touching the current one to see if we 
            can move the whole line of boxes
        """
        # the next row and col are a box: we need to continue to
        # explore in the same direction to see when the boxes stop
        visited = set()
        robot_new_row, robot_new_col = row, col
        dr, dc = self.directions[move]
        while self.grid[row][col] == 'O':
            visited.add((row, col))
            new_row, new_col = row + dr, col + dc
            row, col = new_row, new_col
            if self.grid[new_row][new_col] == '#':
                return False
        # now move box using visited
        for r, c in visited:  # shift all in the same direction as we were moving
            self.grid[r+dr][c+dc] = 'O'
        self.grid[robot_new_row][robot_new_col] = '@'
        return True

    def find_robot_initial_pos(self) -> tuple[int]:
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.grid[row][col] == '@':
                    return row, col

    def generate_new_grid(self):
        """
            Create grid with new shape.
        """
        self.new_grid = [['.'] * self.num_cols *
                         2 for i in range(self.num_rows)]
        # create borders
        for col in range(len(self.new_grid[0])):
            self.new_grid[0][col] = '#'
            self.new_grid[self.num_rows-1][col] = '#'
        for row in self.new_grid:
            row[:2] = ['#'] * 2
            row[-2:] = ['#'] * 2
        # populate grid
        for row in range(1, len(self.original_grid)-1):
            for col in range(1, len(self.original_grid[0])-1):
                if 0 <= row < len(self.original_grid) and 0 <= col < len(self.original_grid[0]):
                    if self.original_grid[row][col] == '#':
                        self.new_grid[row][2*col] = "#"
                        self.new_grid[row][2*col+1] = "#"
                    elif self.original_grid[row][col] == 'O':
                        self.new_grid[row][2*col] = '['
                        self.new_grid[row][2*col+1] = ']'
                        continue
                    elif self.original_grid[row][col] == '@':
                        self.new_grid[row][2*col] = '@'
                        if self.new_grid[row][2*col+1] in ['[', '#']:
                            continue
        return

    def move_robot_part2(self, move: str, row: int, col: int) -> bool:
        if not (0 <= row < self.num_rows_new_grid and 0 <= col < self.num_cols_new_grid):
            return False
        # check new position
        if self.new_grid[row][col] == '#':
            return False
        if self.new_grid[row][col] == '[' or self.new_grid[row][col] == ']':
            return self.move_box_part2(move, row, col)
        else:
            # updated robot position
            self.grid[row][col] = '@'
            r, c = self.visited_q_new.popleft()
            self.new_grid[r][c] = '.'
            self.visited_q_new.append((row, col))
            return True

    def move_box_part2(self, move: str, row: int, col: int) -> bool:
        """
            handle moving both parts of box
            there will be 4 cases which we need to process differently
            dependening on the move we need to make
        """
        visited = set()
        robot_new_row, robot_new_col = row, col
        dr, dc = self.directions[move]
        value = self.new_grid[row][col]
        to_visit = self.is_valid_move(row, col, dr, dc, value)

        # shift boxes we visited
        for r, c in to_visit:
            pass

    def part1(self):
        gps_score = 0
        row, col = self.robot_initial_pos
        for move in self.moves:
            # get instruction
            dr, dc = self.directions[move]
            new_row, new_col = row + dr, col + dc
            valid_move = self.move_robot(move, new_row, new_col)
            if valid_move:
                self.grid[row][col] = '.'
                row, col = new_row, new_col
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.grid[row][col] == 'O':
                    gps_score += self.compute_distance(row, col)
        return gps_score

    def part2(self):
        """
            New rules for moving robot:
            moving right and hit [, need to same as 0 rule
            except we need to check for ] followed by [.
            - Stack for valid values
            if we approach from above or below we will hit either [ or ]
            and we need to move both but also check for # values.
        """
        self.generate_new_grid()
        self.num_rows_new_grid = len(self.new_grid)
        self.num_cols_new_grid = len(self.new_grid[0])
        gps_score = 0
        row, col = self.robot_initial_pos
        row = row * 2  # updated posiion
        for move in self.moves:
            # get instruction
            dr, dc = self.directions[move]
            new_row, new_col = row + dr, col + dc
            valid_move = self.move_robot_part2(move, new_row, new_col)
            if valid_move:
                self.new_grid[row][col] = '.'
                row, col = new_row, new_col
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.new_grid[row][col] == '[':
                    gps_score += self.compute_distance(row, col)
        return gps_score

    def main(self):

        # Solve parts
        print("Part 1:", self.part1())
        print("Part 2:", self.part2())


if __name__ == "__main__":
    sol = Solution()
    sol.main()

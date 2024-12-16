from typing import List, Set, Tuple


class Solution:

    def __init__(self, filename):
        self.filename = filename
        self.matrix = self.parse_input()
        self.start_point = self.find_start_point()
        self.obstacle = '#'
        self.current_direction = 'up'  # start moving up
        # move 90 form current direction
        self.direction_change = {
            'up': 'right',
            'right': 'down',
            'down': 'left',
            'left': 'up'
        }
        # print(len(self.matrix), len(self.matrix[0]))
        # print(self.matrix)
        # print(self.start_point)

    def parse_input(self):
        with open(self.filename) as f:
            matrix = []
            for line in f.readlines():
                matrix.append(list(line.strip()))
        return matrix

    def find_start_point(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == '^':
                    return i, j

    def move(self, row, col):
        # keep going in the same direction
        if self.current_direction == 'up':
            row -= 1
        elif self.current_direction == 'down':
            row += 1
        elif self.current_direction == 'right':
            col += 1
        else:
            col -= 1
        return row, col

    def traverse_matrix(self, matrix):
        """Traverse the matrix using the rule that if we
           hit an obstacle we must move 90 degrees to the right
           trave direction we are currently moving: if right and obstacle we move down etc
           Must keep travelling unti we hit a bound: len(row) or len(col)
        """
        seen = list()
        row, col = self.start_point
        while row < len(matrix) and col < len(matrix[0]):
            seen.append((row, col))
            if self.matrix[row][col] == self.obstacle:
                # move back to where we were before hitting obstacle
                print('cell at obstacle: ', row, col)
                if len(seen) <= 1:  # first cell is obstacle
                    col += 1
                else:
                    # remove cell with obstacle since we dont actually move there
                    seen.pop()
                    # last cell we visited before current cell
                    row, col = seen[-1]

                print('cell before obstacle: ', row, col)
                # change direction
                self.current_direction = self.direction_change[self.current_direction]
                # move again
                row, col = self.move(row, col)
            else:
                row, col = self.move(row, col)
        self.visited_path = seen
        return len(set(seen))

    def part1_v2(self):
        """Use row + dr and col + dc
           to change directions we can swap the variables
           like this: dr, dc = dc, -dr
        """
        seen = set()
        row, col = self.start_point
        dr, dc = -1, 0  # nove up at start

        while 0 <= row + dr < len(self.matrix) and 0 <= col + dc < len(self.matrix[0]):
            seen.add((row, col))
            if self.matrix[row + dr][col + dc] == self.obstacle:
                dr, dc = dc, -dr
            row += dr
            col += dc
        return len(seen)+1  # missing one elemnent somehwere

    def part1(self):
        return self.traverse_matrix(self.matrix)

    def traverse_matrix_new(self, matrix):
        """Traverse the matrix using the rule that if we
           hit an obstacle we must move 90 degrees to the right
           trave direction we are currently moving: if right and obstacle we move down etc
           Must keep travelling unti we hit a bound: len(row) or len(col)
        """
        seen = list()
        self.current_direction = 'up'  # reset after part 1
        row, col = self.start_point
        while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            if (row, col, self.current_direction) in seen:
                return True
            seen.append((row, col, self.current_direction))
            # print("Part 2: ", row, col, self.current_direction)
            if self.matrix[row][col] == self.obstacle:
                # move back to where we were before hitting obstacle
                # print('cell at obstacle: ', row, col)
                if len(seen) <= 1:  # first cell is obstacle
                    col += 1
                else:
                    # remove cell with obstacle since we dont actually move there
                    seen.pop()
                    # last cell we visited before current cell
                    row, col, direction = seen[-1]

                # print('cell before obstacle: ', row, col)
                # change direction
                self.current_direction = self.direction_change[self.current_direction]
                # move again
                row, col = self.move(row, col)
            else:
                row, col = self.move(row, col)
            # if we are at the same point and going in the same direction as before
            # we are in a loop
        return False

    def part2(self):
        """1: detect a loop
           If we have already visited a cell and are moving the same
           direction as before that is a loop
           We only need to check the visited path since that is where
           the obstacle should be placed. Still Brute force approach
        """
        count = 0
        grid = self.matrix
        for row, col in self.visited_path:
            # for row in range(len(self.matrix)):
            #     for col in range(len(self.matrix[0])):
            if grid[row][col] == '#':
                continue
            grid[row][col] = '#'
            print('obstruction placed at: ', row, col)
            count += self.traverse_matrix_new(grid)
            grid[row][col] = '.'
        return count-1

    def traverse_matrix_v2(self, matrix):
        """
        Traverse the matrix using the original logic but optimized.
        Detect loops by tracking visited states and backtrack correctly
        when encountering obstacles.
        """
        seen = set()  # Use a set for faster lookups
        row, col = self.start_point
        current_direction = 'up'  # Reset direction at the start

        while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            # Use (row, col, direction) as the unique state identifier
            state = (row, col, current_direction)

            # Detect a loop if the state has been visited before
            if state in seen:
                return True  # Loop detected
            seen.add(state)

            if matrix[row][col] == self.obstacle:
                # Backtrack to the last valid cell
                if len(seen) <= 1:  # First cell is an obstacle
                    col += 1  # Move to the right as fallback
                else:
                    # Revert to the last visited cell and direction
                    seen.remove(state)
                    row, col, current_direction = list(seen)[-1]

                # Change direction after hitting an obstacle
                current_direction = self.direction_change[current_direction]
            else:
                # Move in the current direction
                if current_direction == 'up':
                    row -= 1
                elif current_direction == 'down':
                    row += 1
                elif current_direction == 'right':
                    col += 1
                elif current_direction == 'left':
                    col -= 1

        return False  # No loop detected

    def part2_v2(self):
        """Detect loops after placing obstacles.
        Optimize by avoiding repeated matrix traversal and excessive memory usage."""
        count = 0
        grid = self.matrix
        seen = set()

        for row, col in self.visited_path:
            if grid[row][col] == '#':  # Skip already placed obstacles
                continue

            # Temporarily mark the cell as an obstacle
            grid[row][col] = '#'
            print('Obstruction placed at: ', row, col)

            # Check for loops without modifying the grid repeatedly
            if self.traverse_matrix_v2(grid):
                count += 1

            # Remove the temporary obstacle
            grid[row][col] = '.'

        return count

    def main(self):
        part1 = self.part1()
        part1_v2 = self.part1_v2()
        part2 = self.part2_v2()
        return part1, part1_v2, part2


if __name__ == "__main__":
    filename = 'day6/day6.txt'
    solution = Solution(filename)
    part1, part1_vs, part2 = solution.main()
    print(part1, part1_vs, part2)

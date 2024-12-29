import argparse
from typing import List, Set, Tuple
import os
import sys
from collections import deque, defaultdict
import heapq as heap

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))


class Solution:

    def __init__(self):
        with open(sys.argv[1]) as f:
            #self.grid = list(map(str.strip, f.readlines()))
            self.grid = [list(line.strip()) for line in f.readlines()]

        self.num_rows, self.num_cols = len(self.grid), len(self.grid[0])
        self.starting_position = self.find_starting_point()
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        print(self.starting_position)
        # costs from different directions
        self.cost_map = {}

    def find_starting_point(self):
        for r, row in enumerate(self.grid):
            for c, val in enumerate(row):
                if val == 'S':
                    return r, c

    def find_shorest_path(self):
        cost = 0

        def bfs(row: int, col: int):
            """
                - visted set 
                - queue
                - search in all directions:
                - Need to keep track of the visited path in the queue but
                  the final visited cell will be used to explore next cells:
                  append to q the full path so far + [new_row, new_col]
            """
            q = deque([[(row, col)]])
            visited = set()

            while len(q) > 0:
                path = q.popleft()
                row, col = path[-1]
                if self.grid[row][col] == 'E':
                    return path  # will contain entire path we took
                if self.grid[row][col] == '#':
                    continue
                for dr, dc in self.directions:  # add all neighbours to queue
                    new_row, new_col = row + dr, col + dc
                    if (new_row, new_col) not in visited and self.grid[new_row][new_col] != '#':
                        visited.add((new_row, new_col))
                        q.append(path + [(new_row, new_col)])
        # will return all points visted to get to the goal
        shortest_path = bfs(
            self.starting_position[0], self.starting_position[1])
        return shortest_path

    def part1(self):
        def dijkstra(row: int, col: int):
            """row, col will starting cell
            """
            # cost, starting r and col and direction: i.e. facing right
            pq = [(0, row, col, 0, 1, [(row, col)])]
            seen = {(row, col, 0, 1)}
            points = set()
            best_cost = float('inf')

            while pq:
                cost, row, col, dr, dc, path = heap.heappop(pq)
                # each time iteration we add to the previous best path
                # cheapest way to get to the current point due to pq
                seen.add((row, col, dr, dc))
                if self.grid[row][col] == 'E':
                    # we do not return immediately since we want
                    # to sure for all paths with the lowest cost
                    return cost, path

                    # direction we move has different costs: turning trick
                    # clockwise: r, c = c, -r : e.g. facing up and turning right: (-1, 0) -> (0, 1)
                    # counter clockwise: r, c = -c, r: facing up and turning left: (-1, 0) -> (0, -1)
                    # turning does not move to a new tile: this is why row and col dont change
                direction_costs = [
                    (cost + 1, row + dr, col + dc, dr, dc),  # moving forward
                    (cost + 1000, row, col, dc, -dr),  # clockwise turn
                    (cost + 1000, row, col, -dc, dr)  # counter clockwise turn
                ]
                # loop through directions we can move
                for new_cost, nr, nc, ndr, ndc in direction_costs:
                    if self.grid[nr][nc] == '#':
                        continue
                    if (nr, nc, ndr, ndc) in seen:
                        continue
                    heap.heappush(
                        pq, (new_cost, nr, nc, ndr, ndc, path + [(nr, nc)]))
        cost, path = dijkstra(*self.starting_position)
        # print(cost, path)
        return cost, path

    def part2(self):
        """
            We need all possible paths with the lowest cost.
            In part 1 we returned after finding the best path, now
            we must also check paths with <= cost as the best one.
            We just need to keep track of the current path by adding it to
            the heap. Once we find E we check if the cost <= best cost
            and add all points on the path to a points set.
        """
        points = set()

        def djikstra_v2(row: int, col: int):
            best_cost = float('inf')
            # cost, row, col, dr, dc, path
            pq = [(0, row, col, 0, 1, [(row, col)])]
            seen = {(row, col, 0, 1)}

            while pq:
                cost, row, col, dr, dc, path = heap.heappop(pq)
                seen.add((row, col, dr, dc))
                if self.grid[row][col] == 'E':
                    # dont return immediately, we need all points with lowest cost
                    if cost <= best_cost:
                        best_cost = cost
                        for point in path:
                            points.add(point)

                # check directional movements: turning does not actually move onto a new tile so
                # we do not increase row or col
                direction_costs = [
                    (cost + 1, row + dr, col + dc, dr, dc),  # moving forward
                    (cost + 1000, row, col, dc, -dr),  # clockwise turn
                    (cost + 1000, row, col, -dc, dr)  # counter clockwise turn
                ]
                for new_cost, nr, nc, ndr, ndc in direction_costs:
                    if self.grid[nr][nc] == '#':
                        continue
                    if (nr, nc, ndr, ndc) in seen:
                        continue
                    heap.heappush(pq,
                                  (new_cost, nr, nc, ndr,
                                   ndc, path + [(nr, nc)])
                                  )
            return points
        points = djikstra_v2(*self.starting_position)
        return len(points)

    def main(self):
        # Solve parts
        print("Part 1:", self.part1())
        print("Part 2:", self.part2())


if __name__ == "__main__":
    sol = Solution()
    sol.main()

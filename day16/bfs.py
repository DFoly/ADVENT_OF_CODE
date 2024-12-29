from collections import deque


def in_bounds(row: int, col: int, num_rows: int, num_cols: int) -> bool:
    return 0 <= row <= num_rows and 0 <= col <= num_cols


def traverse_array(arr: list[int]):
    starting_point = (3, 0)
    end_point = (0, 6)
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    num_rows, num_cols = len(arr), len(arr[0])

    def bfs(row: int, col: int):
        """
            - queue
            - visited set
            - directions: get neighbours
            - append to queue
        """
        visited = set()
        q = deque([[(row, col)]])

        while q:
            path = q.popleft()
            row, col = path[-1]
            visited.add((row, col))
            if (row, col) == end_point:
                return path, visited
            for dr, dc in directions:
                rr, cc = row+dr, col+dc
                if not in_bounds(rr, cc, num_rows, num_cols) or (rr, cc) in visited:
                    continue
                visited.add((rr, cc))
                q.append(path+[(rr, cc)])
        return path, visited
    path, visited = bfs(*starting_point)
    return path


if __name__ == '__main__':
    array = [
        [1, 3, 5, 6, 8, 9],
        [20, 4, 98, 11, 13, 3],
        [0, 4, 7, 4, 6, 8],
        [10, 98, 4, 2, 8, 7],
    ]
    ans = traverse_array(array)
    print(ans)

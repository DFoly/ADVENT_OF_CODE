# Advent of Code - Day 12

## Problem Description

Paste the problem description here.

## Running the Solution

### Using Main Input:
```bash
python solution.py
```

### Using Test Input:
```bash
python solution.py --test
```

### Solution
- seems like we need to do a BFS or DFS and count the number of plots
- we also need to keep track of perimeter values: for each direction we move we increase
the perimeter value for the plot unless we are moving to the same value
# Advent of Code - Day 10

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

## Solution Notes
- We can probaby do this using BFS: the problem is very similar to number of islands
- Instead of searching for 1's we search for a sequence
- we can visit cells more than once as trails can overlap as per examples
- find starting cells of all 0's and begin search from there.
- Trail head starts at 0: we want to count the number of unique 9's we can reach from each trail head
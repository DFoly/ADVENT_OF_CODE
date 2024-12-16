# Advent of Code - Day 8

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

## Scratch Work
- Using example

..........
...#...... (1,3)
..........
....a..... (3, 4)
..........
.....a.... (5, 5)
..........
......#... (7,6)
..........
..........

(5,5) - (3,4) = (2,1)
point 1 # = (3,4) - (2,1) = (1,3)
point 2 # = (5,5) + (2,1) = (7,6)

### Solution Attempt
- we loop through the matrix and save the location of all antennas of the same type: 'A': [(1,2), (4,5)] etc
- For each Antenna type we compute the distance between them all
- We then create antinodes by using points +- the differences if they are within the grid

### Part 2
- seems like we keep adding antinodes distance teh same delta from the points while we are in the grid
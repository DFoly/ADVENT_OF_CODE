# Advent of Code - Day 9

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


## Thoughts on Solution
- example: 2333133121414131402
- Need to be able to loop through numbers: regex findall(/d+): each digit in list
- 12345
- odd numbers represent: file blocks
- even numbers represent free space
- id: 0, 1 block file, 2 free space
- id: 1, 3 block file 4 free space
- id: 2 5 block file
- this is encoded as: 0..111....22222

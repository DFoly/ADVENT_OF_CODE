import argparse
from typing import List, Set, Tuple
import os
import re

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))


class Solution:
    def __init__(self):
        self.grid = list()

    def calculate_check_sum(self, result: list) -> int:
        """
        """
        cumulative_total = 0
        for id, value in enumerate(result):
            if value == '.':
                continue
            cumulative_total += id * value
            #sprint(id, value, cumulative_total)
        return cumulative_total

    def swap_algorithm_part1(self, result_list: list) -> list:
        left, right = 0, len(result_list)-1
        while left < right:
            if result_list[left] != '.':
                left += 1
            elif result_list[right] == '.':
                right -= 1
            else:
                result_list[left], result_list[right] = result_list[right], result_list[left]
                left += 1
                right -= 1
        return result_list

    def part_algo(self, results):
        """
            Output will be new array with files in correct place: while current_id >= 0
            while list not empty we pop off element get length of group: i.e. 99
            Then find memory space for it to the left of 99 and swap values
        """
        current_id = results[-1]
        self.visited = set()

        file_blocks = self.precompute_file_blocks(results)

        for current_id in sorted(file_blocks.keys(), reverse=True):

            # get memory block of same size as file
            mem_block_results = self.get_memory_blocks(results)
            # print(mem_block_results)

            # try and insert the current file block into
            results = self.insert_file_block(
                current_id, results, file_blocks, mem_block_results)
            current_id -= 1
            # print(results)
        return results

    def precompute_file_blocks(self, results):
        """Precompute all file block positions and sizes."""
        file_blocks = {}
        i = len(results) - 1
        while i >= 0:
            if results[i] != '.':
                current_id = results[i]
                block_end = i
                while i >= 0 and results[i] == current_id:
                    i -= 1
                block_start = i + 1
                file_size = block_end - block_start + 1
                file_blocks[int(current_id)] = (
                    block_start, block_end, file_size)
            else:
                i -= 1
        return file_blocks

    def get_memory_blocks(self, results) -> list:
        """
            Find and store the locations of each memory block
            hash_map: (x,y): len(block)
        """
        mem_block_results = []
        start = i = 0
        while i < len(results) - 1:
            if results[i] == '.':
                start = i
                while results[i] == '.' and i < len(results)-1:
                    i += 1
                # indices key and len values: i-1 to get end of mem block
                # needs to be ordered to ensure we store in left most memory
                mem_block_results.append((start, i-1, i-start))
            else:
                i += 1
        return mem_block_results

    def insert_file_block(self, current_id: int, results: list,
                          hash_map_file_blocks: dict, mem_block_results: list):
        """
        Given a file block and memory address and size we want to
        insert the file block into this location
        """
        start_idx, end_idx, file_size = hash_map_file_blocks[current_id]
        for i in mem_block_results:
            # if memory > size of file we insert the block
            # can only insert to the left
            if i[2] == file_size and (i[0], i[1]+1) < (start_idx, end_idx):
                for j in range(file_size):
                    results[i[0] + j], results[start_idx +
                                               j] = results[start_idx + j], results[i[0] + j]
            elif i[2] > file_size and (i[0], i[1]+1) < (start_idx, end_idx):
                # slice swapping actually makes sublists: below is in place
                for j in range(file_size):
                    results[i[0] + j], results[start_idx +
                                               j] = results[start_idx + j], results[i[0] + j]
                return results
        return results

    def part1(self):
        """
        """
        check_sum = 0
        cols = len(self.data)
        id_count = 0
        result_list = []
        block_inputs = range(0, cols, 2)  # every second value
        free_space_inputs = range(1, cols, 2)
        for col in range(cols):
            if col in block_inputs:
                block_files = [id_count] * self.data[col]
                result_list.extend(block_files)
                id_count += 1
            elif col in free_space_inputs:
                free_space_block = ['.'] * self.data[col]
                result_list.extend(free_space_block)
        # self.grid.append(result_list)
        # swap the memory into the correct place
        new_result_list = self.swap_algorithm_part1(result_list)
        check_sum += self.calculate_check_sum(new_result_list)
        return check_sum

    def part2(self):
        check_sum = 0
        cols = len(self.data)
        id_count = 0
        result_list = []
        block_inputs = range(0, cols, 2)  # every second value
        free_space_inputs = range(1, cols, 2)
        for col in range(cols):
            if col in block_inputs:
                block_files = [id_count] * self.data[col]
                result_list.extend(block_files)
                id_count += 1
            elif col in free_space_inputs:
                free_space_block = ['.'] * self.data[col]
                result_list.extend(free_space_block)
        # self.grid.append(result_list)
        # swap the memory into the correct place
        new_result_list = self.part_algo(result_list)
        #new_result_list = [i for i in new_result_list if i != '.']
        check_sum += self.calculate_check_sum(new_result_list)
        return check_sum

    def main(self):
        # Parse command-line arguments
        parser = argparse.ArgumentParser(description="Advent of Code Day 9")
        parser.add_argument('--t', action='store_true',
                            help="Use test input instead of main input")
        args = parser.parse_args()

        # Select input file
        filename = "test.txt" if args.t else "input.txt"
        # Construct paths relative to the script directory
        self.filename = os.path.join(script_dir, filename)
        self.data = []
        with open(self.filename) as f:
            for line in f.readlines():
                self.data = [int(i) for i in line]
        # print(self.data)
        # Solve parts
        print("Part 1:", self.part1())
        print("Part 2:", self.part2())


if __name__ == "__main__":
    sol = Solution()
    sol.main()

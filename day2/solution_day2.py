from typing import List

class SolutionDay2:

    def __init__(self, filename):
        with open(filename) as file:
            self.data = file.read()

    def is_safe(self, seq: List[int]) -> bool:
        """
        Check if abs values between numbers are
        within 1-3.
        Also Check if all differences are > 0 or < 0 
        for continous sequence
        """
        deltas = [a-b for a,b in zip(seq, seq[1:])]
        is_monotonic = all(i > 0 for i in deltas) or all(i < 0 for i in deltas)
        is_range = all(1 <= abs(i) <= 3 for i in deltas)
        if is_monotonic and is_range:
            return True
        return False
        
    
    def is_safe_dampner(self, seq: List[int]) -> bool:
        """
            If we initially fail the is_safe
            we run another check where we remove
            iteratively remove 1 item from the seq
            and check is_safe again, if its safe
            we break the loop for that seq and increase
            the safe count
        """
        # iteratively remove items from seq
        for i in range(len(seq)):
            # remove 1 item and create new array
            new_seq = seq[:i] + seq[i+1:]
            if self.is_safe(new_seq):
                return True
        return False
    
    def part1(self):
        """

        """
        self.safe_count = 0
        for line in self.data.split('\n'):
            seq = [int(i) for i in line.split()]
            self.safe_count += self.is_safe(seq)
        return self.safe_count

    
    def part2(self):
        """
        """
        self.safe_count = 0
        for line in self.data.split('\n'):
            seq = [int(i) for i in line.split()]
            is_safe = self.is_safe(seq)
            if is_safe: # another check for removing items
                self.safe_count += 1
            else:
                self.safe_count += self.is_safe_dampner(seq)
        return self.safe_count
    

    def main(self):
        """
        
        """
        part1_result = self.part1()
        part2_result = self.part2()
        return part1_result, part2_result
    

if __name__=='__main__':
    filename = 'day2/day2.txt'
    sol = SolutionDay2(filename)

    part1_result, part2_result = sol.main()
    print(part1_result, part2_result)
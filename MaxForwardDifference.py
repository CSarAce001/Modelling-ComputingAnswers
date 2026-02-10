# A forward difference of a sequence of numbers is the difference B − A of two numbers in the sequence, where B occurs
# after A in the sequence. E.g., in the sequence (10, 6, 12, 15), the number 5 is a forward difference (15 − 10) but 4 is
# not (even though 4 = 10 − 6, 10 does not precede 6 in the sequence).
# One possible application could be in stock trading: if we have a list of predicted stock prices, then a forward difference
# would represent the profit that could be made by first buying a share, and then later on selling it again. Of course,
# we want to make as much profit as possible, so we would like to figure out what the maximum forward difference of
# the sequence is.
# The goal of this assignment is to practice with divide and conquer by applying that technique to compute the maximum
# forward difference of a sequence.

#No way


import sys

def main():
    # Read input
    input_data = sys.stdin.read().split()
    iterator = iter(input_data)
    
    # Number of testcases
    num_cases = int(next(iterator))
    
    # Handle all testcases
    for _ in range(num_cases):
        # Number of inputs in testcase
        length = int(next(iterator))
        
        # Read sequence
        sequence = []
        for _ in range(length):
            sequence.append(int(next(iterator)))
        
        # Do computation and print output
        # result is expected to be a tuple: (mfd_value, index_low, index_high)
        result = mfd_divide_and_conquer(sequence, 0, length)
        print(f"{result[0]} {result[1]} {result[2]}")


def mfd_divide_and_conquer(sequence, low, high):
    # Calculates the Maximum Forward Difference of the sequence
    # sequence[low]...sequence[high - 1] using Divide and Conquer
    # Returns a tuple: (mfd, index_of_min, index_of_max)
    
    if low == high - 1:
        # Base case: sequence of length 1
        # It contains only sequence[low]
        # A single element cannot have a difference
        # TODO: Return a base case tuple
        # Since MFD requires two numbers, you might want to return a very small number
        # for the MFD value here to ensure it's not chosen as the maximum later
        return (float('-inf'), low, low)
    
    mid = (low + high) // 2
    
    # Apply divide and conquer to two halves of the sequence
    # Each call returns (mfd_value, index_low, index_high) for half the original sequence
    result_left = mfd_divide_and_conquer(sequence, low, mid)
    result_right = mfd_divide_and_conquer(sequence, mid, high)
    
    # 1. Find the Minimum value (and its index) in the LEFT half
    min_left_val = sequence[low]
    min_left_idx = low
    for i in range(low + 1, mid):
        if sequence[i] < min_left_val:
            min_left_val = sequence[i]
            min_left_idx = i
    
    # 2. Find the Maximum value (and its index) in the RIGHT half
    max_right_val = sequence[mid]
    max_right_idx = mid
    for i in range(mid + 1, high):
        if sequence[i] > max_right_val:
            max_right_val = sequence[i]
            max_right_idx = i
    
    # 3. Calculate the MFD that spans both halves (crossing the midpoint)
    mfd_spanning = max_right_val - min_left_val
    
    # 4. Compare all three possibilities and return the maximum
    # The MFD is either entirely in the left half, entirely in the right half,
    # or spans both halves (buy in left, sell in right)
    candidates = [
        result_left,
        result_right,
        (mfd_spanning, min_left_idx, max_right_idx)
    ]
    
    # Find and return the result with the maximum MFD value
    final_result = max(candidates, key=lambda x: x[0])
    
    return final_result


if __name__ == "__main__":
    main()
from typing import List
import sys

def largest_product(nums : List[int]) -> int:
    p = -sys.maxsize - 1
    for i in range(len(nums) - 1):
        if (nums[i] * nums[i + 1]) > p:
            p = nums[i] * nums[i + 1]

    return p

inputList = [3, 6, -2, -5, 7, 3]
print(largest_product(inputList))
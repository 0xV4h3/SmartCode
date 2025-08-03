from typing import List

def filter(numbers: List[int]) -> List[int]:
    if not numbers:
        return []
    elif len(numbers) == 1:
        if numbers[0] % 2 == 0:
            return [numbers[0]]
        else:
            return []
    else:
        mid = len(numbers) // 2
        return filter(numbers[:mid]) + filter(numbers[mid:])

nums = [7, 4, 10, 2, 5, 6, 3, 8, 7, 1, 5]
print(filter(nums))

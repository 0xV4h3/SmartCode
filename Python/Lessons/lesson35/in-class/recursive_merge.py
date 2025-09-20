from typing import List

def merge(lst1: List[int], lst2: List[int]) -> List[int]:
    if not lst1: return lst2
    if not lst2: return lst1
    return [lst1[0]] + merge(lst1[1:], lst2) if lst1[0] <= lst2[0] else [lst2[0]] + merge(lst1, lst2[1:])

if __name__ == "__main__":
    print(merge([1, 4, 7, 11, 14], [2, 3, 6, 11, 13, 17]))
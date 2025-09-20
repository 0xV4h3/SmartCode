from typing import List

def symmetric(grid: List[List[int]]) -> bool:
    n = len(grid)
    for i in range(n):
        for j in range(i+1, n):
            if grid[i][j] != grid[j][i]:
                return False
    return True

if __name__ == "__main__":
    print(symmetric([[1]]))
    print(symmetric([[1, 2], [2, 5]]))
    print(symmetric([[1, 2], [1, 1]]))
    print(symmetric([[1, 2, 3], [2, 4, 5], [3, 5, 6]]))

from typing import List

class Matrix:
    def __init__(self, nrows: int, ncols: int):
        self.nrows: int = nrows
        self.ncols: int = ncols
        self.data: List[List[int]] = [[0]*ncols for r in range(nrows)]

    def max(self, other) -> "Matrix":
        if isinstance(other, Matrix):
            r = min(self.nrows, other.nrows)
            c = min(self.ncols, other.ncols)

            max_matrix = Matrix(r, c)

            for i in range(r):
                for j in range(c):
                    max_matrix.data[i][j] = max(self.data[i][j], other.data[i][j])
            return max_matrix
        return NotImplemented

if __name__ == "__main__":
    a = Matrix(3, 3)
    b = Matrix(2, 4)

    a.data = [
        [1, 9, 5],
        [4, 2, 8],
        [7, 6, 3]
    ]
    b.data = [
        [3, 1, 10, 4],
        [5, 7,  2, 0]
    ]

    c = a.max(b)

    print("Matrix A:", a.data)
    print("Matrix B:", b.data)
    print("Max matrix:", c.data)
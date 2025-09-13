# Custom Array Filters
# https://www.codewars.com/kata/53fc954904a45eda6b00097f

from typing import List
import sys

class list(list):

    def even(self) -> List[int]:
        return [n for n in self if isinstance(n, int) and n % 2 == 0]

    def odd(self) -> List[int]:
        return [n for n in self if isinstance(n, int) and n % 2 == 1]

    def under(self, limit: int) -> List[int]:
        return [n for n in self if isinstance(n, int) and n < limit]

    def over(self, limit: int) -> List[int]:
        return [n for n in self if isinstance(n, int) and n > limit]

    def in_range(self, lower: int = -sys.maxsize - 1, upper: int = sys.maxsize) -> List[int]:
        return [n for n in self if isinstance(n, int) and (lower <= n <= upper)]

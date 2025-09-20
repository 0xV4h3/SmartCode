import math
from typing import List

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def add_primes(vals: List[int]) -> int:
    if not vals: return 0
    return (vals[0] if is_prime(vals[0]) else 0) + add_primes(vals[1:])

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    print(f"Primes sum : {add_primes(nums)}")

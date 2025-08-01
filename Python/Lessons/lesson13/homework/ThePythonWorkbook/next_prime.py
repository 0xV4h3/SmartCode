# 99 from The Python Workbook
from is_prime import is_prime

def nextPrime(num : int) -> int:
    num += 1
    while not is_prime(num):
        num += 1
    return num

if __name__ == "__main__":
    number = int(input("Enter number: "))
    print(f"First prime number larger than {number}: {nextPrime(number)}")
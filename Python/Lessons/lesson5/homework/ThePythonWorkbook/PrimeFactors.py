#80 from The Python Workbook
import math

def prime_factors(number, separator=" "):
    if number < 2:
        print("No prime factors.")
        return

    factors = []

    while number % 2 == 0:
        factors.append("2")
        number = number // 2

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            factors.append(str(i))
            number = number // i

    if number > 2:
        factors.append(str(number))

    print(separator.join(factors))

if __name__ == '__main__':
    n = int(input("Enter number: "))
    prime_factors(n, "\n")

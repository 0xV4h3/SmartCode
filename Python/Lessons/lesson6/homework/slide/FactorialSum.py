import math

def factorial_iterative(number):
    if number < 0:
        return "Factorial is not defined for negative numbers."
    elif number == 0:
        return 1
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result


if __name__ == '__main__':
    num = input("Enter number: ")
    while not num.isdigit():
        num = input("Enter number again: ")

    num = int(num)

    sum1 = 0
    sum2 = 0

    for i in range(1, num + 1):
        sum1 += math.factorial(i)
        sum2 += factorial_iterative(i)

    if sum1 == sum2:
        print(f"Sum of factorials of numbers from 1 to {num} : {sum1}")


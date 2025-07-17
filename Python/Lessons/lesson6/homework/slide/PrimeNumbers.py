import math

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, (int(math.sqrt(number)) + 1)):
        if number % i == 0:
            return False

    return True

if __name__ == '__main__':
    count = input("Enter the count of numbers: ")
    while not count.isdigit():
        count = input("Enter count again: ")

    count = int(count)

    prime_numbers = 0

    for _ in range(count):
        num = input("Enter number: ")
        while not num.isdigit():
            num = input("Enter number again: ")

        num = int(num)
        if is_prime(num):
            prime_numbers += 1

    print(f"Count of prime numbers in sequence: {prime_numbers}")



#79 from The Python Workbook
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    number_one = int(input("Enter first number : "))
    number_two = int(input("Enter second number : "))

    print(f"Greatest common divisor of {number_one} and {number_two} is {gcd(number_one, number_two)}")
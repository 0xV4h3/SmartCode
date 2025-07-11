def factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers."
    elif number == 0:
        return 1
    else:
        fact = 1
        for i in range(1, number + 1):
            fact *= i
        return fact

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print(f"Factorial od {n} is {factorial(n)}")
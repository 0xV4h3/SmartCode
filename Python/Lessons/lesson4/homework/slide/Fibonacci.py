def fibonacci(n, delimiter = " "):
    if n <= 0:
        print("Please enter a positive integer for the number of terms.")
        return
    elif n == 1:
        print(0, end=delimiter)
        return

    a, b = 0, 1
    print(a, end=delimiter)
    print(b, end=delimiter)

    for i in range(2, n):
        fib_number = a + b
        print(fib_number, end=delimiter)
        a, b = b, fib_number
    print()

if __name__ == '__main__':
    print("Fibonacci sequence")
    sequence = int(input("Enter a count of numbers in sequence: "))
    separator = input("Enter a delimiter symbol: ")

    fibonacci(sequence, separator)
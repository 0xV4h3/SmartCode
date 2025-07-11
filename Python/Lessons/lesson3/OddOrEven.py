def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    number = int(input('Enter a number: '))
    if isEven(number):
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")

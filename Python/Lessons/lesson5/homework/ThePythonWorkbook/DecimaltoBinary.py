#82 from The Python Workbook
def decimal_to_binary(number):
    if number == 0:
        return "0000"
    binary = ""
    while number != 0:
        binary += str(number % 2)
        number //= 2

    binary = binary[::-1]
    binary = binary.zfill((len(binary) + 3) // 4 * 4)
    return binary

if __name__ == '__main__':
    n = int(input("Enter number: "))
    print(f"Decimal {n} - Binary {decimal_to_binary(n)}")
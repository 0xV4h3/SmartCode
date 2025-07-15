#81 from The Python Workbook
def binary_to_decimal(binary) -> int:
    if binary.count('0') + binary.count('1') != len(binary):
        print("Invalid digit/symbol in binary string")
        return 0
    position = 0
    number = 0
    reverse = binary[::-1]
    for bit in reverse:
        if bit == '1':
            number += 2 ** position
        position += 1

    return number

if __name__ == '__main__':
    binary_string = input("Enter binary string:")

    while binary_string.count('0') + binary_string.count('1') != len(binary_string):
        binary_string = input("Enter binary string:")

    print(f"Binary {binary_string} - Decimal {binary_to_decimal(binary_string)}")
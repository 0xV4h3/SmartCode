#70 from The Python Workbook
count = int(input("Enter count of bytes: "))

for _ in range(count):
    line = input("Enter 8-bit binary string: ")

    if len(line) != 8 or line.count("0") + line.count("1") != 8:
        print("Invalid input. Must be exactly 8 binary digits.")
        continue

    ones = line.count("1")

    if ones % 2 == 0:
        print("Parity bit (even): 0")
    else:
        print("Parity bit (even): 1")

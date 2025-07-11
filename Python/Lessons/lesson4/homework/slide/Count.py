number = int(input("Enter a number: "))
number_string = str(number)

count = 0
for digit in number_string:
    count += int(digit)

print(f"Count of digits in number {number} is {count}")

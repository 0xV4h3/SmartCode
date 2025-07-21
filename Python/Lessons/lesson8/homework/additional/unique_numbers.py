# ex3
numbers = []
unique_numbers = set()
repeating_numbers = set()

number = input("Enter number: ")
while number != '' and number.isdigit():
    numbers.append(int(number))
    number = input("Enter number: ")

for number in numbers:
    if number not in unique_numbers and number not in repeating_numbers:
        unique_numbers.add(number)
    elif number in unique_numbers and number not in repeating_numbers:
        unique_numbers.remove(number)
        repeating_numbers.add(number)
    elif number not in repeating_numbers:
        repeating_numbers.add(number)


if not numbers:
    print("There is no number")
else:
    print(f"Numbers: {numbers}")
    if not unique_numbers:
        print(f"All numbers are repeating: {repeating_numbers}")
    else:
        if not repeating_numbers:
            print(f"All numbers are unique: {unique_numbers}")
        else:
            print(f"Unique numbers: {unique_numbers}")
            print(f"Repeating numbers: {repeating_numbers}")
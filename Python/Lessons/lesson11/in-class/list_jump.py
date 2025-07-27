numbers = []

number = input("Enter number: ")
while number != '' and number.isdigit():
    numbers.append(int(number))
    number = input("Enter number: ")

print(numbers)
i = 0
while i < len(numbers):
    if i == len(numbers) - 1:
        print(True)
        break
    elif numbers[i] == 0 or numbers[i + numbers[i]] >= len(numbers):
        print(False)
        break
    else:
        i += numbers[i]

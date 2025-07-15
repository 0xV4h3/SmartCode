#63 from The Python Workbook
average = 0.0
summ = 0
count = 0
while True:
    number = int(input("Enter number: "))
    if number == 0:
        average = summ / count
        break
    else:
        summ += number
        count += 1

print(f"Average: {average}")

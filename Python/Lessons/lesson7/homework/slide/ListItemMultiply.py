num_list = []

while True:
    number = input("Enter number: ")
    if number.isdigit():
        num_list.append(int(number))
    else:
        break

multiplication = 1
for i in range(len(num_list)):
    multiplication *= num_list[i]

print(f"List: {num_list}")
print(f"Multiplication of items of the list: {multiplication}")




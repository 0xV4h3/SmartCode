num_list = []
odds = []

while True:
    number = input("Enter number: ")
    if number.isdigit():
        num_list.append(int(number))
    else:
        break

print(f"Number list before deletion of evens: {num_list}")

for i in range(len(num_list) - 1, -1, -1):
    if num_list[i] % 2 == 1:
        odds.insert(0,num_list[i])
    else:
        num_list.pop(i)

if not odds:
    print("No odd number in Num list")
else:
    if num_list == odds:
        print(f"Number list after deletion of evens: {num_list}")
    else:
        print("Something is wrong")
        print(f"Num list: {num_list}")

    print(f"Odd numbers: {odds}")
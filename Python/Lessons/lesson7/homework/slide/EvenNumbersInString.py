numbers = input("Enter numbers: ")
str_list = numbers.split()
num_list = []

for str_nums in str_list:
    num_list.append(int(str_nums))

even = []

for number in num_list:
    if number % 2 == 0:
        even.append(number)

print(f"Input: {num_list}")
if not even:
    print("No even number in Input")
else:
    print(f"output: {even}")
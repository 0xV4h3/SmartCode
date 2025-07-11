number_one = int(input("Enter first number : "))
number_two = int(input("Enter second number : "))

greater = max(number_one, number_two)
limit = (number_one * number_two) + 1

for i in range(greater, limit, greater):
    if i % number_one == 0 and i % number_two == 0:
        print(f"LCM is {i}")
        break
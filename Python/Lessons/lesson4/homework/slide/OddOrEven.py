def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

even_count = 0
odd_count = 0

for number in range(1, 100):
    if isEven(number):
        even_count += 1
    else:
        odd_count += 1

print(f"Even numbers count in 1-100 : {even_count}")
print(f"Odd numbers count in 1-100  : {odd_count}")
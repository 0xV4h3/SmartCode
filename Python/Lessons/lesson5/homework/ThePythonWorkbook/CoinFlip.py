#84 from The Python Workbook
import random

iterations = 10
tries_list = []

for i in range(iterations):
    occurrences = 0
    last_flip = ''
    tries_list.append(0)
    while occurrences != 3:
        tries_list[i] += 1
        coin = random.choice(['H', 'T'])
        print(coin, end=" ")
        if coin == last_flip:
            occurrences += 1
        else:
            last_flip = coin
            occurrences = 1
    print(f"({tries_list[i]} flips)")

summ = 0

for tries in tries_list:
    summ += tries

average = summ/iterations

print(f"On average, {average} flips were needed.")





import random

group = []
pulled_names = []

name = input("Enter name: ")
while name != '':
    group.append(name)
    name = input("Enter text: ")

pulled = ""
for name in group:
    pulled = random.choice(group)
    while pulled == name or pulled in pulled_names:
        pulled = random.choice(group)

    pulled_names.append(pulled)

for i in range(len(group)):
    print(f"{group[i]} pulled {pulled_names[i]}")



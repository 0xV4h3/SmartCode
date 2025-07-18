items = []
item = input("Enter item: ")

while item != '':
    items.append(item)
    item = input("Enter item: ")

print(f"Items: {items}")

for i in range(len(items) - 1, -1, -1):
    for j in range(len(items) - 1, i, -1 ):
        if items[j] == items[i]:
            items.pop(j)

print(f"Unique items: {items}")
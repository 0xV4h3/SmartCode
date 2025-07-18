laptops = []
taget = "Mac"

laptop = input("Enter laptop: ")
while laptop != '':
    laptops.append(laptop)
    laptop = input("Enter laptop: ")

print(laptops)

if taget in laptops:
    print(True)
else:
    print(False)
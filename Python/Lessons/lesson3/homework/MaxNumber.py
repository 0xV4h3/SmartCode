x = int(input('Enter x: '))
y = int(input('Enter y: '))

print((x + y + abs(x - y)) // 2)

print(y ^ ((x ^ y) & -(x > y)))

print((x > y) * x + (x <= y) * y)

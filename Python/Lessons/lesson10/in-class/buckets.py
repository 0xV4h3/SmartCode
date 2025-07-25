lines = {}
lines_number = int(input("Enter the number of lines: "))

for i in range(lines_number):
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    lines[i] = (x, y)

print("Lines:", lines)

max_surface = 0

for i in range(lines_number - 1):
    x1, y1 = lines[i]
    for j in range(i + 1, lines_number):
        x2, y2 = lines[j]
        width = abs(x2 - x1)
        height = min(y1, y2)
        surface = width * height
        if surface > max_surface:
            max_surface = surface

print(f"Max surface: {max_surface}")

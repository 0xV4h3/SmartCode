def century(year : int) -> int:
    return (year - 1) // 100 + 1

y = int(input('Input year : '))
while y < 1:
    y = int(input('Input year : '))

print(f"Year {y} in century {century(y)}")
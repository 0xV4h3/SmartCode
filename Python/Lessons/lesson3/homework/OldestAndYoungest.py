first = int(input("Enter age of first man : "))
second = int(input("Enter age of second man : "))
third = int(input("Enter age of third man : "))

if first > second:
    if first > third:
        if second > third:
            print(f"First man is oldest({first}), and third man is youngest({third}).")
        else:
            print(f"First man is oldest({first}), and second man is youngest({second}).")
    else:
        print(f"Third man is oldest({third}), and second man is youngest({second}).")
else:
    if second > third:
        if first > third:
            print(f"Second man is oldest({second}), and third man is youngest({third}).")
        else:
            print(f"Second man is oldest({second}), and first man is youngest({first}).")
    else:
        print(f"Third man is oldest({third}), and first man is youngest({first}).")

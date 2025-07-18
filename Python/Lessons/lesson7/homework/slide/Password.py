special_characters = ('!', '@', '#', '$', '%', '&', '*')
min_len = 9
spec_char_count = 0
num_count = 0

password = input("Enter password: ")
if len(password) >= min_len:
    for char in password:
        if char in special_characters:
            spec_char_count += 1
        elif char.isdigit():
            num_count += 1

    if spec_char_count >= 2 and num_count >= 2:
        print("Strong")
    else:
        print("Weak")
else:
    print("Weak")

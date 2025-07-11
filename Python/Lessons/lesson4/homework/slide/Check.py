user_age = int(input("Enter user age: "))
user_sex = input("Enter user sex: ")

if 18 <= user_age <= 20:
    if user_sex.lower() == "male":
        print("User is valid")
    else:
        print("Invalid user")
else:
    print("Invalid user")
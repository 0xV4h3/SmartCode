user_age = int(input("Enter your age: "))
user_sex = input("Enter your sex(M/F): ")
user_marital_status = input("Enter your marital status(Y/N): ")

if user_sex == "F":
    print(f"Female employee with Age {user_age} will work only in urban areas.")
elif user_sex == "M":
    if (user_age > 20) and (user_age < 40):
        print(f"Male employee with Age {user_age} may work in anywhere.")
    elif (user_age > 40) and (user_age < 60):
        print(f"Male employee with Age {user_age} will work in urban areas only.")
else:
    print("ERROR")


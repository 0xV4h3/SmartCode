# 103 from The Python Workbook
from check_a_password import is_good
from random_password import random_password

def main():
    attempts = 1
    password = random_password()
    print(f"{attempts} : {password}")
    while not is_good(password):
        attempts += 1
        password = random_password()
        print(f"{attempts} : {password}")
    print(f"Number of attempts that were needed to generate good password: {attempts}")


if __name__ == "__main__":
    main()
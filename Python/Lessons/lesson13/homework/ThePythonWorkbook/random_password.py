# 100 from The Python Workbook
import random

def random_password() -> str:
    length = random.randint(7, 10)
    password = ''
    for _ in range(length):
        password += chr(random.randint(33, 126))
    return password

if __name__ == "__main__":
    print(random_password())
    print(random_password())
# 101 from The Python Workbook
import random

def random_license_plate() -> str:
    relevance = random.choice(('old', 'new'))
    license_plate = ''
    if relevance == 'old':
        for _ in range(3):
            license_plate += chr(random.randint(65, 90))
        for _ in range(3):
            license_plate += chr(random.randint(48, 57))
    else:
        for _ in range(4):
            license_plate += chr(random.randint(48, 57))
        for _ in range(3):
            license_plate += chr(random.randint(65, 90))
    return license_plate

if __name__ == "__main__":
    print(random_license_plate())
    print(random_license_plate())
    print(random_license_plate())
    print(random_license_plate())
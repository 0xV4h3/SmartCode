# 102 from The Python Workbook
def is_good(password : str) -> bool:
    if len(password) < 8:
        return False
    upper = False
    lower = False
    digit = False
    for symbol in password:
        if symbol.isupper() and not upper:
            upper = True
        elif symbol.islower() and not lower:
            lower = True
        elif symbol.isdigit() and not digit:
            digit = True

    if upper and lower and digit:
        return True
    return False

if __name__ == "__main__":
    print(is_good('qwerty11'))
    print(is_good('Admin2026'))
    print(is_good('********'))
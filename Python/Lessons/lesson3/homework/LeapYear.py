def isLeapYear(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

if __name__ == '__main__':
    year = int(input('Enter a year: '))
    if isLeapYear(year):
        print(f"The {year} is leap year.")
    else:
        print(f"The {year} is not leap year.")

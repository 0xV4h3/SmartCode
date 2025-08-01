# 109 from The Python Workbook
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

def magic_date(day : int, month : int, year : int) -> bool:
    return True if (day * month) == (year % 100) else False

if __name__ == "__main__":
    magic_dates = []
    for year in range(1900, 2000):
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if isLeapYear(year):
            month_days[1] = 29
        for month in range(1, 13):
            for day in range(1, month_days[month - 1] + 1):
                if magic_date(day, month, year):
                    magic_dates.append((day, month, year))

    print("Magic dates in XX century")
    for day, month, year in magic_dates:
        print(f"{day}/{month}/{year}")



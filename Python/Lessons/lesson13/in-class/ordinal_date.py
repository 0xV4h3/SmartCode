# 91 from The Python Workbook
def ordinalDate(day : int, month : int, year : int) -> int:
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
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeapYear(year):
        month_days[1] = 29
    day_of_the_year = day
    if month == 1:
        return day
    else:
        for i in range(0, month - 1):
            day_of_the_year += month_days[i]
    return day_of_the_year

if __name__ == "__main__":
    day = int(input("Enter day: "))
    month= int(input("Enter month: "))
    year = int(input("Enter year: "))
    print(f"Day of the year: {ordinalDate(day, month, year)}")
# 92 from The Python Workbook
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

def ordinalDate(day : int, month : int, year : int) -> int:
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

def gregorian_date(year : int, day_of_the_year : int) -> (int, int, int):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_a_year = 365
    if isLeapYear(year):
        month_days[1] = 29
        days_in_a_year = 366
    month = 1
    if day_of_the_year <= 31:
        return 31, 0, year
    elif day_of_the_year > 31 and day_of_the_year <= days_in_a_year:
        for i in range(0, 12):
            if day_of_the_year <= month_days[i]:
                break
            else:
                day_of_the_year -= month_days[i]
                month += 1
    else:
        while day_of_the_year > month_days[month - 1]:
            day_of_the_year -= days_in_a_year
            year += 1
            if isLeapYear(year):
                month_days[1] = 29
                days_in_a_year = 366
            else:
                month_days[1] = 28
                days_in_a_year = 365
            if day_of_the_year <= days_in_a_year:
                for i in range(0, 12):
                    if day_of_the_year <= month_days[i]:
                        break
                    else:
                        day_of_the_year -= month_days[i]
                        month += 1
    return day_of_the_year, month, year

def due_date(day : int, month : int, year : int) -> (int, int, int):
    gestation_period = 280
    first_day = ordinalDate(day, month, year)
    return gregorian_date(year, first_day + gestation_period)

if __name__ == "__main__":
    months_dict = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    print("First day date(day/month/year)")
    day = int(input("Enter day: "))
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))
    due_day, due_month, due_year = due_date(day, month, year)
    print(f"Due date: {due_day}/{months_dict[due_month]}/{due_year}")

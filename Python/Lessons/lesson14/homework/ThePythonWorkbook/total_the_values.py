# Exercise 173:Total the Values
def total_values() -> int:
    number = input("Enter number: ")
    if number == '':
        return 0
    number = int(number)
    return number + total_values()

if __name__ == "__main__":
    print(total_values())
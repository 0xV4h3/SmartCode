# Exercise 175: Recursive Decimal to Binary
def decimal_to_binary(number : int) -> str:
    if number == 0 or number == 1:
        return str(number)
    else:
        return decimal_to_binary(number // 2) + str(number % 2)

if __name__ == "__main__":
    num = int(input("Enter number: "))
    if num < 0:
        print(f"{num} if negative")
    else:
        print(decimal_to_binary(num))
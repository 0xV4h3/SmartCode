def digits_sum(number) -> int:
    digitssum = 0
    for digit in str(number):
        digitssum += int(digit)
    return digitssum

if __name__ == '__main__':
    count = input("Enter the count of numbers: ")
    while not count.isdigit():
        count = input("Enter count again: ")

    count = int(count)
    max_sum = 0
    max_sum_number = 0

    for _ in range(count):
        num = input("Enter number: ")
        while not num.isdigit():
            num = input("Enter number again: ")

        num = int(num)
        dig_sum = digits_sum(num)
        if dig_sum > max_sum:
            max_sum = dig_sum
            max_sum_number = num

    print(f"{max_sum_number} have maximum sum of digits: {max_sum}")
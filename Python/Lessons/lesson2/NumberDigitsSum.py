def digits_sum(number) -> int:
    digitssum = 0
    for digit in str(number):
        digitssum += int(digit)
    return digitssum

if __name__ == '__main__':
    print(f"Sum of your numbers digits: {digits_sum(input('Enter a number: '))}")



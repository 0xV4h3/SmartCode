# #69 from The Python Workbook
# toddlers = 0
# children = 14
# adult = 23
# pensioner =  18
# revenue = 0.0
#
# while True:
#     age = input("Enter age: ")
#     if age == '':
#         break
#     else:
#         age = int(age)
#         if age < 0:
#             print("Error")
#         elif 3 <= age <= 12:
#             revenue += children
#         elif 12 < age <= 65:
#             revenue += adult
#         elif age > 65:
#             revenue += pensioner
#
# print(f"Revenue: {round(revenue, 2)}")
#
#
# import math
#
# def prime_factors(number, separator = " "):
#     while number % 2 == 0:
#         print(2, end=separator)
#         number = number / 2
#
#     for i in range(3, int(math.sqrt(number)) + 1, 2):
#
#         while number % i == 0:
#             print(i, end=separator)
#             number = number / i
#     if number > 2:
#         print(number, end=separator)
#
# if __name__ == '__main__':
#     n = int(input("Enter number: "))
#     prime_factors(n)

# def digits_sum(number) -> int:
#     digitssum = 0
#     for digit in str(number):
#         digitssum += int(digit)
#     return digitssum
#
# if __name__ == '__main__':
#     n = input('Enter a number: ')
#     dig_sum = digits_sum(n)
#     print(f"Digits sum: {dig_sum}")
#     while len(str(dig_sum)) != 1:
#         dig_sum = digits_sum(dig_sum)
#         print(f"Digits sum: {dig_sum}")

# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#
# def lcm(a, b):
#     return abs(a * b) // gcd(a, b)
#
# number_one = int(input("Enter first number : "))
# number_two = int(input("Enter second number : "))
#
# print(lcm(number_one, number_two))

# number_one = int(input("Enter first number : "))
# number_two = int(input("Enter second number : "))
#
# greater = max(number_one, number_two)
# limit = (number_one * number_two) + 1
#
# for i in range(greater, limit, greater):
#     if i % number_one == 0 and i % number_two == 0:
#         print(f"LCM is {i}")
#         break

# text = input("Enter text: ")
# letters = 0
# digits = 0
# symbols = 0
# for char in text:
#     if char.isalpha():
#         letters += 1
#     elif char.isdigit():
#         digits += 1
#     else:
#         symbols += 1
#
# print(f"Letters : {letters}\nDigits : {digits}\nSymbols : {symbols}\n")

# import random
#
# current_max = random.randint(1, 100)
# print(current_max)
# for i in range(1, 99):
#     number = random.randint(1, 100)
#     if number > current_max:
#         print(f"{number} - update")
#         current_max = number
#     else:
#         print(number)

# import math
#
# def is_prime(number):
#     if number <= 1:
#         return False
#
#     for i in range(2, (int(math.sqrt(number)) + 1)):
#         if number % i == 0:
#             return False
#
#     return True
#
# a = int(input("Enter number: "))
#
# if is_prime(a):
#     print(f"{a} is prime")
# else:
#     print(f"{a} is not prime")

# pi = 3
# numerator = 4
# denominator_start = 2
#
# for i in range(1, 15):
#     first_fraction = numerator / (denominator_start * (denominator_start + 1) * (denominator_start + 2))
#     temp = denominator_start + 2
#     second_fraction = numerator / (temp * (temp + 1) * (temp + 2))
#     denominator_start = temp + 2
#     pi += (first_fraction - second_fraction)
#
# print(f"Pi : {pi}")

# BG GB : BGB X 1G - 2B max
# BG GB : BGG GBG GGB : BGGG GBGG GGBG GGGB .... infinit G - 1B
# GB BG : GBB
# 


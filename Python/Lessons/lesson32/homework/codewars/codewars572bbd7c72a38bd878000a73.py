# Implement the Fractions class
# https://www.codewars.com/kata/572bbd7c72a38bd878000a73
from math import gcd

class Fraction:

    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator

    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num

    def __str__(self):
        return f'{self.top}/{self.bottom}'

    def __add__(self, other):
        if isinstance(other, Fraction):
            numerator = (self.top * other.bottom) + (other.top * self.bottom)
            denominator = self.bottom * other.bottom
            frac_gcd = gcd(numerator, denominator)
            return Fraction(numerator//frac_gcd, denominator//frac_gcd)
        return NotImplemented

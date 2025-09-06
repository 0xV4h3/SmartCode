class Calculator:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.number + other.number)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.number - other.number)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.number * other.number)
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.number // other.number)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.number / other.number)
        return NotImplemented

    def __mod__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.number % other.number)
        return NotImplemented

    def __pow__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.number ** other.number)
        return NotImplemented

    def __str__(self):
        return f'{self.number}'

a = Calculator(2)
b = Calculator(3)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a ** b)

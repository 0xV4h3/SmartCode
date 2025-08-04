# Exercise 174: Greatest Common Divisor
def gcd(a : int, b: int) -> int:
    if b == 0:
        return a
    else:
        c = a % b
        return gcd(b, c)

if __name__ == "__main__":
    print(gcd(10078954, 80256))
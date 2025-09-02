class RealString(str):
    def __lt__(self, other):
        if isinstance(other, str):
            return len(self) < len(other)
        return False

    def __le__(self, other):
        if isinstance(other, str):
            return len(self) <= len(other)
        return False

    def __eq__(self, other):
        if isinstance(other, str):
            return len(self) == len(other)
        return False

    def __ne__(self, other):
        if isinstance(other, str):
            return len(self) != len(other)
        return False

    def __gt__(self, other):
        if isinstance(other, str):
            return len(self) > len(other)
        return False

    def __ge__(self, other):
        if isinstance(other, str):
            return len(self) >= len(other)
        return False

a = RealString("Zip")
b = RealString("Apple")

print(a > b)
print(a < b)
print(a == b)
print(RealString("cat") == RealString("dog"))



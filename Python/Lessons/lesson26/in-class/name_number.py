import math

class NameNumber:
    mapping = {
        1: "ajs", 2: "bkt", 3: "clu",
        4: "dmv", 5: "enw", 6: "fox",
        7: "gpy", 8: "hqz", 9: "ir"
    }

    letter_to_num = {ch: num for num, chars in mapping.items() for ch in chars}

    def __init__(self, name: str):
        self.name = name.lower()
        self.value = sum(self.letter_to_num.get(ch, 0) for ch in self.name)

    def is_widespread(self) -> str:
        return "Yes" if math.sqrt(self.value) < 5 else "No"

    def __str__(self):
        return f"{self.value}, {self.is_widespread()}"

print(NameNumber("Anna"))
print(NameNumber("Ani"))
print(NameNumber("Michael"))
print(NameNumber("Jon"))
print(NameNumber("Shakira"))
print(NameNumber("Kim"))


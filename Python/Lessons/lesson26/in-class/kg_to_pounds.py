class KgToPounds:
    coeff = 2.20462

    def __init__(self, kg: int = 0):
        self.__kg = kg if kg > 0 else 0

    def get_kg(self) -> int:
        return self.__kg

    def set_kg(self, kg: int):
        self.__kg = kg if kg > 0 else 0

    def to_pounds(self):
        return self.__kg * KgToPounds.coeff

converter = KgToPounds()
converter.set_kg(10)
print(converter.to_pounds())
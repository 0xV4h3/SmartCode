from math import pi

class CoronaTest:
    def corona_test(self, temperature: float) -> str:
        num = round(temperature * pi)
        if 120 <= num <= 128:
            return 'You have coronavirus'
        return 'Everything is ok'

cor_test = CoronaTest()
print(cor_test.corona_test(36.6))
print(cor_test.corona_test(39))

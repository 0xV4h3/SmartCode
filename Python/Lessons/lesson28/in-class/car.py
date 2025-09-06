class Car:
    base1 = 200
    base2 = 300
    base3 = 500
    additional_limit = 150
    additional_tax = 1000

    def __init__(self, mark : str, model : str, year : int, color : str, hp : int, price: float):
        self.mark = mark
        self.model = model
        self.year = year
        self.color = color
        self.hp = hp
        self.price = price

    def tax(self) -> int:
        if 1 <= self.hp <= 120:
            return self.hp * Car.base1
        elif 121 <= self.hp <= 250:
            return self.hp * Car.base2 if self.hp <= Car.additional_limit else self.hp * Car.base2 + (self.hp - Car.additional_limit) * Car.additional_tax
        else:
            return self.hp * Car.base3 if self.hp <= Car.additional_limit else self.hp * Car.base3 + (self.hp - Car.additional_limit) * Car.additional_tax


car = Car('Mercedes', 'CLS630', 2015, 'black mate', 100, 30000)
print(car.tax())
car = Car('Mercedes', 'CLS630', 2015, 'black mate', 150, 30000)
print(car.tax())
car = Car('Mercedes', 'CLS630', 2015, 'black mate', 170, 30000)
print(car.tax())
car = Car('Mercedes', 'CLS630', 2015, 'black mate', 260, 30000)
print(car.tax())
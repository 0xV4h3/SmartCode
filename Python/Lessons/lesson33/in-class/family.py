import random
from abc import ABC, abstractmethod

class House:
    money = 100
    human_food = 50
    cat_food = 30
    dirt = 0

class Human(ABC):
    def __init__(self, satiety):
        self.satiety = satiety if satiety > 0 else 100

    def eat(self):
        if House.human_food >= 10:
            self.satiety += 10
            House.human_food -= 10
        else:
            self.satiety -= 10

class Man(Human):
    def work(self):
        self.satiety -= 10
        House.money += 50

    def play(self):
        self.satiety -= 10

    def eat(self):
        super().eat()

    def is_alive(self):
        return self.satiety > 0

class Woman(Human):
    def __init__(self, satiety, coeff=1):
        super().__init__(satiety)
        self.coeff = coeff

    def update_coeff(self):
        if House.dirt > 90:
            self.coeff = 1.5
        else:
            self.coeff = 1

    def buy_food(self):
        if House.money >= 30:
            House.money -= 30
            House.human_food += 30

    def buy_cat_food(self):
        if House.money >= 10:
            House.money -= 10
            House.cat_food += 10

    def clean_house(self):
        House.dirt = max(0, House.dirt - 100)
        self.satiety -= int(10 * self.coeff)

    def eat(self):
        super().eat()

    def is_alive(self):
        return self.satiety > 0

class Animal(ABC):
    def __init__(self, satiety):
        self.satiety = satiety if satiety > 0 else 100

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

class Cat(Animal):
    def eat(self):
        if House.cat_food >= 10:
            self.satiety += 20
            House.cat_food -= 10
        else:
            self.satiety -= 10

    def sleep(self):
        self.satiety -= 10

    def tear_wallpaper(self):
        self.satiety -= 10
        House.dirt += 5

    def is_alive(self):
        return self.satiety > 0

def simulate():
    Murka = Cat(100)
    Nikita = Man(100)
    Nastya = Woman(100)

    for day in range(1, 366):
        House.dirt += random.randint(1, 6)
        Nikita.satiety -= 10
        Nastya.update_coeff()
        Nastya.satiety -= int(10 * Nastya.coeff)
        Murka.satiety -= 10

        dead = []
        if not Nikita.is_alive():
            dead.append("Husband")
        if not Nastya.is_alive():
            dead.append("Wife")
        if not Murka.is_alive():
            dead.append("Cat")
        if dead:
            print(f'{" and ".join(dead)} died on day {day}! The family did not survive.')
            print(f'Status: Husband {Nikita.satiety}, Wife {Nastya.satiety}, Cat {Murka.satiety}')
            print(f'House: Money {House.money}, Human Food {House.human_food}, Cat Food {House.cat_food}, Dirt {House.dirt}')
            return

        husband_action = random.choice(['work', 'play', 'eat'])
        if husband_action == 'work':
            Nikita.work()
        elif husband_action == 'play':
            Nikita.play()
        elif husband_action == 'eat':
            Nikita.eat()

        wife_action = random.choice(['buy_food', 'buy_cat_food', 'clean_house', 'eat'])
        if wife_action == 'buy_food':
            Nastya.buy_food()
        elif wife_action == 'buy_cat_food':
            Nastya.buy_cat_food()
        elif wife_action == 'clean_house':
            Nastya.clean_house()
        elif wife_action == 'eat':
            Nastya.eat()

        cat_action = random.choice(['eat', 'tear_wallpaper', 'sleep'])
        if cat_action == 'eat':
            Murka.eat()
        elif cat_action == 'tear_wallpaper':
            Murka.tear_wallpaper()
        elif cat_action == 'sleep':
            Murka.sleep()

    print('The family and the cat survived a year! Hooray!')
    print(f'Status: Husband {Nikita.satiety}, Wife {Nastya.satiety}, Cat {Murka.satiety}')
    print(f'House: Money {House.money}, Human Food {House.human_food}, Cat Food {House.cat_food}, Dirt {House.dirt}')

if __name__ == '__main__':
    simulate()
from typing import Optional
import copy

class Human:
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"{self.name}, {self.age} years old, {self.gender}, {self.height}cm/{self.weight}kg"

    def __repr__(self):
        return (f"Human(name={self.name!r}, age={self.age}, "
                f"gender={self.gender!r}, height={self.height}, weight={self.weight})")

class People:
    attributes = ['name', 'age', 'gender', 'height', 'weight']

    def __init__(self, people : list["Human"] = None):
        self.people = people if people is not None else []

    def append(self, human : "Human"):
        self.people.append(human)

    def pop(self, index : int = -1):
        self.people.pop(index)

    def clear(self):
        self.people = []

    def sort(self, by : str = 'gender', gen = 'male', reverse_order = False) -> Optional[list["Human"]]:
        if by in People.attributes:
            sorted_people = []
            if by == 'name':
                sorted_people = copy.deepcopy(self.people)
                sorted_people.sort(reverse=reverse_order,key=lambda human: human.name)
            elif by == 'age':
                sorted_people = copy.deepcopy(self.people)
                sorted_people.sort(reverse=reverse_order, key=lambda human: human.age)
            elif by == 'gender':
                sorted_people = [human for human in self.people if human.gender == gen]
            elif by == 'height':
                sorted_people = copy.deepcopy(self.people)
                sorted_people.sort(reverse=reverse_order, key=lambda human: human.height)
            elif by == 'weight':
                sorted_people = copy.deepcopy(self.people)
                sorted_people.sort(reverse=reverse_order, key=lambda human: human.weight)
            return sorted_people
        return None

mard1 = Human('Boris', 24, 'male', 180, 75)
mard2 = Human('Anna', 22, 'female', 164, 52)
mardik = People([mard1, mard2])

print("By gender")
print(mardik.sort(by = 'gender', gen ='female'))
print(mardik.sort(by = 'gender'))
print("Order")
print(mardik.sort(by = 'name'))
print(mardik.sort(by = 'age'))
print(mardik.sort(by = 'height'))
print(mardik.sort(by = 'weight'))
print("Reverse order")
print(mardik.sort(by = 'name', reverse_order=True))
print(mardik.sort(by = 'age', reverse_order=True))
print(mardik.sort(by = 'height', reverse_order=True))
print(mardik.sort(by = 'weight', reverse_order=True))



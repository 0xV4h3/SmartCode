# Smart Traffic Lights
# https://www.codewars.com/kata/58587905ed1b4dad6e0000c6
from typing import Optional

class SmartTrafficLight:
    def __init__(self, st1, st2):
        self.st1 = st1
        self.st2 = st2

    def turngreen(self) -> Optional[str]:
        if self.st1[0] > self.st2[0]:
            road = self.st1[1]
            self.st1[0] = 0
            return road
        elif self.st1[0] < self.st2[0]:
            road = self.st2[1]
            self.st2[0] = 0
            return road
        return None


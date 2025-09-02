import random
from typing import List

class HarryPotterFight:
    spells = ["Avada Kedavra", "Crucio", "Imperio"]

    def __init__(self, attempts : List):
        self.harry_spells= attempts
        self.voldemort_spells = [random.choice(self.spells) for _ in range(len(self.harry_spells))]

    def fight(self):
        score = 0
        attempts_match = 0
        for i in range(len(self.harry_spells)):
            if self.harry_spells[i] == self.voldemort_spells[i]:
                score += 1
                attempts_match += 1
            else:
                score -= 1

        result = "You win" if score >= 1 and attempts_match >= 2 else "You lose"
        return " ".join(self.voldemort_spells), result

fight = HarryPotterFight([
    "Avada Kedavra",
    "Crucio",
    "Imperio"
])

voldemort_spells, result = fight.fight()
print(voldemort_spells)
print(result)

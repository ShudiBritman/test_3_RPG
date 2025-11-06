import random

from core.player import Players


class Monsters(Players):
    weapons = ["Knife", "Sword", "Ax"]
    value_weapons = {
        "Knife": 0.5,
        "Sword": 1,
        "Ax": 1.5}
    def __init__(self):
        super().__init__()
        self.type = None
        self.num_index = random.randint(0, 2)
        self.weapon = Monsters.weapons[self.num_index]

    def speak(self):
        print(f"{self.type}, is furious")


    def attack(self):
        pass

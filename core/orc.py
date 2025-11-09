import random

from .player import Player
from .monsters import Monsters


class Orc(Monsters):
    def __init__(self):
        super().__init__()
        self.name = "Sofia Richie"
        self.hp = 50
        self.type = "orc"
        self.speed = random.randint(0, 5)
        self.power = random.randint(10, 15)
        self.armor_rating = random.randint(2, 8)

    def speak(self):
        super().speak()

    def attack(self, player, monster):
        speed = self.roll_dice(20)
        speed += self.speed
        if speed > player.armor_rating:
            self.damage_calculator(monster, player)
            return True
        else:
            return False

    def damage_calculator(self, winner, looser):
        dice = self.roll_dice(6)
        value = winner.power * Monsters.value_weapons[winner.weapon]
        looser.hp -= value + dice


    def roll_dice(self, sides:int):
        num = random.randint(0, sides)
        return num


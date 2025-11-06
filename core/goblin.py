import random
import game
from core.monsters import Monsters


class Goblin(Monsters):
    def __init__(self):
        super().__init__()
        self.name = "Rox"
        self.hp = 20
        self.type = "goblin"
        self.speed = random.randint(5, 10)
        self.power = random.randint(5, 10)
        self.armor_rating = 1

    def speak(self):
        super().speak()

    def attack(self):
        def attack(self, player, monster):
            speed = game.Game.roll_dice(20)
            speed += player.speed
            if speed > player.armor_ratung:
                self.damage_calculator(monster, player)
                return True
            else:
                return False

        def damage_calculator(self, winner, looser):
            dice = self.roll_dice(6)
            value = winner.power * Monsters.value_weapons[winner.weapon]
            looser.hp -= value + dice
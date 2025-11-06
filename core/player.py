import random
from abc import abstractmethod
import game


class Players:
    def __init__(self, ):
        self.name = None
        self.speed = None
        self.power = None
        self.armor_rating = None
        num_index = None
        self.profession = None
        self.hp = None

    @abstractmethod
    def speak(self):
        pass



class Player(Players):
    professions = ["fighter", "cure"]
    def __init__(self):
        super().__init__()
        self.name = "Eli"
        self.speed = random.randint(5, 10)
        self.power = random.randint(5, 10)
        self.armor_rating = random.randint(5, 15)
        num_index = random.randint(0, 1)
        self.profession = Player.professions[num_index]
        if self.profession == Player.professions[0]:
            self.hp = 50
        else:
            self.hp = 60

    def speak(self):
        print(f"Hello I'm {self.name}")

    def attack(self, player, monster):
        speed = game.Game.roll_dice(20)
        speed += player.speed
        if speed > monster.armor_ratung:
            self.damage_calculator(player, monster)
            return True
        else:
            return False

    def damage_calculator(self, winner, looser):
        dice = self.roll_dice(6)
        looser.hp -= winner.power + dice





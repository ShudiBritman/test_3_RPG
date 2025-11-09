import random
from abc import abstractmethod


class Players:
    def __init__(self, ):
        self.name = None
        self.speed = None
        self.power = None
        self.armor_rating = None
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
        speed = self.roll_dice(20)
        speed += self.speed
        if speed > monster.armor_rating:
            self.damage_calculator(player, monster)
            return True
        else:
            return False

    def damage_calculator(self, winner, looser):
        dice = self.roll_dice(6)
        looser.hp -= winner.power + dice



    def roll_dice(self, sides:int):
        num = random.randint(0, sides)
        return num





import random
import core.player
import core.orc
import core.goblin

class Game:
    def __init__(self):
        self.won = None


    def start(self):
        player = self.create_player()
        play = self.show_menu()
        if play == "p":
            monster = self.choose_random_monster()
            player.speak()
            monster.speak()
            state = self.battle(player, monster)
            print(f"Winner is {self.won}")


    def show_menu(self):
        play = input("Do you want to play? press 'p' for play, or 'e' to exit")
        return play


    def create_player(self):
        player = core.player.Player
        return player


    def choose_random_monster(self):
        monsters = ["Orc", "Goblin"]
        choose_monster = monsters[random.randint(0, 1)]
        if choose_monster == "Orc":
            monster = core.orc.Orc()
        else:
            monster = core.goblin.Goblin()

        return monster

    def organizer_battle(self, current_player, other):
        state = 0
        won = 0
        while not won:
            attack = current_player.attack(current_player, other)
            if attack:
                self.won = self.is_won(current_player, other)
                temp = current_player
                current_player = other
                other = temp
            else:
                self.won = self.is_won(current_player, other)
                temp = current_player
                current_player = other
                other = temp



    def battle(self, player, monster):
        dice_player = self.roll_dice(6)
        dice_monster = self.roll_dice(6)
        player_speed = player.speed
        monster_speed = monster.speed
        player_state = player_speed + dice_player
        monster_state = monster_speed + dice_monster
        if player_state> monster_state or dice_monster == dice_player:
            self.organizer_battle(player, monster)
        else:
            self.organizer_battle(monster, player)


    def is_won(self,attacks, attacked):
        if attacks.hp > attacked.hp or attacked.hp == 0:
            return True
        else:
            return False


    def roll_dice(self, sides):
        num = random.randint(0, sides)


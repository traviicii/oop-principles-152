from colorama import Fore, Style # pip install colorama
import random
from helper import d, fancy, clear


class Character():

    def __init__(self, name, defense = 50, exp = 0, lvl = 1, hp = 100):
        self.name = name
        self.hp = hp
        self.defense = defense # !!!!?!!?!????!
        self.exp = exp
        self.lvl = lvl
        self.base_damage = 15

    # implement block functionality !!!!

    # implement parry functionality !!!!


    # get character info
    def get_info(self):
        '''Displays character information.'''
        print(f'''
    ~~~~~CHARACTER STATS~~~~~
    {self.name}'s current level: {self.lvl}
    {self.name}'s current  HP: {self.hp}
    {self.name}'s current  EXP: {self.exp}
''')
    
    def level_check(self): # might need to add a parameter for the character we're checking for
        if self.exp >= 100: # leveling up might need to be a function for better useability
                self.lvl += 1
                self.exp -= 100
                print(f"{self.name} just gained a level!!")
                self.get_info()

    def attack(self, target):
        if target.hp <= 0:
            print(f"{target.name} is already dead!!!")
            return
        
        print(f"{Fore.MAGENTA}{self.name} is attacking {target.name}!! {Style.RESET_ALL}")
        # initialize an attack sequence, determine damage value
        damage = self.calculate_damage()
        target.hp -= damage
        if target.hp <= 0:
            print(f"{self.name} has defeated {target.name}!!! {Fore.RED}****FATALITY****{Style.RESET_ALL}")
            self.exp += 20
            self.level_check() # level up??

        else:
            print(f"{self.name} inflicted {damage} damage!!")
            print(f"{target.name}'s remaining HP: {target.hp}") #### make this into a health bar type of thing
            fancy()
            self.get_info()
            d()

    def calculate_damage(self):
        '''Randomize damage based on base damage and consider critical hit'''
        # randomize damage based off of base damage
        damage = random.randint(self.base_damage - 5, self.base_damage + 5)
        if self.critical_hit():
            damage *= 2
            print(f"{self.name} made a {Fore.RED} critical hit!!! {Style.RESET_ALL}")
            return damage
        return damage


    def critical_hit(self):
        # 15% chance for a critical hit
        return random.random() < .15
    

rogue = Character('Aragorn')
warrior = Character('Zelda')

rogue.attack(warrior)
rogue.attack(warrior)
rogue.attack(warrior)
rogue.attack(warrior)
rogue.attack(warrior)
rogue.attack(warrior)
rogue.attack(warrior)
rogue.attack(warrior)
rogue.attack(warrior)


print("|███████████████_________|")
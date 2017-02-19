"""Character creation

Class for character
"""
import time
import random


class Character(object):
    def __init__(self):
        self.name = ''
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.health = 40
        self.points = 20
        self.moves = ['attack', 'dodge', 'block']
        print("Created character... almost")

# =================== Methods for Character ======================

    def user_create_character(self):
        print("Please help finish")
        get_name = input("Please enter name: ")
        self.set_name(get_name)
        print("You have %d points to spend on Attributes:" % (self.points))

    # -------- Distributing the points ----------
        # TODO: Error handling user input
        while True:
            CHARACTER_POINTS_COMMANDS = ['add_points', 'remove_points', 'reset_points']
            self._attributes = {'Strength': self.strength, 'Dexterity': self.dexterity,
                                         'Constitution': self.constitution,
                                         'Intelligence': self.intelligence, 'Wisdom': self.wisdom,
                                         'Charisma': self.charisma}
            self.print_attributes()

            command = input("Enter command to alter points"
                            "(ex. <add,remove>, <attribute>, <amount>"
                            "OR <clear> to reset attributes "
                            "OR <confirm> to finalize character: ")

            numbers_inlist = [x for x in command if x.isdigit()]
            if numbers_inlist:
                amount = int(''.join(numbers_inlist))
            attribute_to_alter = ''
            for key in self._attributes.items():
                if key[0].lower() in command:
                    attribute_to_alter = key[0].lower()
            if 'clear' in command.lower():
                self.reset_points()
                self.print_attributes()
            elif 'add' in command.lower():
                self.add_points(amount, attribute_to_alter)
                self.print_attributes()
            elif 'remove' in command.lower():
                self.remove_points(amount, attribute_to_alter)
                self.print_attributes()
            elif 'confirm' in command.lower():
                self.print_attributes()
                confirmation = input("Are you sure?[y/n] ")
                if confirmation is 'y':
                    break
                else:
                    continue

    # Print for loops
    def print_attributes(self):
        for key, value in self._attributes.items():
            print(key, value)
    def print_commands(self, commands):
        for command in commands:
            print(command, end='')

# ------- Methods to alter points --------
    def add_points(self, amount, attribute):
        if attribute.lower() in 'strength':
            self.strength += amount
            self.points -= amount
        elif attribute.lower() in 'dexterity':
            self.dexterity += amount
            self.points -= amount
        elif attribute.lower() in 'constitution':
            self.constitution += amount
            self.points -= amount
        elif attribute.lower() in 'intelligence':
            self.intelligence += amount
            self.points -= amount
        elif attribute.lower() in 'wisdom':
            self.wisdom += amount
            self.points -= amount
        elif attribute.lower() in 'charisma':
            self.charisma += amount
            self.points -= amount
# TODO: Get remove points to work
# TODO : Make sure that points doesn't go negative
    def remove_points(self, amount, attribute):
        if attribute.lower() in 'strength':
            self.strength -= amount
            self.points += amount
        elif attribute.lower() in 'dexterity':
            self.dexterity -= amount
            self.points += amount
        elif attribute.lower() in 'constitution':
            self.constitution -= amount
            self.points += amount
        elif attribute.lower() in 'intelligence':
            self.intelligence -= amount
            self.points += amount
        elif attribute.lower() in 'wisdom':
            self.wisdom -= amount
            self.points += amount
        elif attribute.lower() in 'charisma':
            self.charisma -= amount
            self.points += amount

    def reset_points(self, attribute):
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.health = 40
        self.points = 20
        
    # Character name methods ----------
    def set_name(self, name):
        self.name = name



# ------- Character Action Methods --------
    def change_name(self):
        new_name = input("Please a new name: ")
        self.name = new_name

    def attack(self, opponent_ac):
        """Character action to damage another
        :return damage
        """
        skill_multiplier = 1
        str_mult = (self.strength-10) / 2
        dex_mult = (self.dexterity-10) /2
        hits = True
        damage = str_mult + skill_multiplier * random.randint(1,4)
    def dodge(self):
        pass
    def block(self):
        pass

if __name__ == '__main__':
    bob = Character()

"""Character creation

Class for character
"""
import time

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
        _attributes = {'Strength': self.strength, 'Dexterity': self.dexterity, 'Constitution': self.constitution,
                       'Intelligence': self.intelligence, 'Wisdom': self.wisdom, 'Charisma': self.charisma}
        print("Creating character...")
        get_name = input("Please enter name: ")
        print("You have %d points to spend on Attributes(MAX:9):" % (self.points))
        self.print_attributes(_attributes)


        # Distributing the points
        CHARACTER_POINTS_COMMANDS = ['add_points', 'remove_points', 'clear_points']
        command = input("Enter command to alter points"
                        "(ex. <add,remove, clear> <attributes><amount>")
        amount = [x for x in command if x.isdigit()]
        if 'clear' in command.lower() :
            pass
        elif 'add' in command.lower():
            pass
        elif 'remove' in command.lower():
            pass



        # while True:
        #     pass

    # Print for loops
    def print_attributes(self,_attributes):
        for key, value in _attributes.items():
            print(key, value)
    def print_commands(self, commands):
        for command in commands:
            print(command, end='')

    # Methods to alter points
    def add_points(self, amount, attribute):
        if attribute.lower() is 'strength':
            self.strength += amount
        elif attribute.lower() is 'dexterity':
            self.dexterity += amount
        elif attribute.lower() is 'constitution':
            self.constitution += amount
        elif attribute.lower() is 'intelligence':
            self.intelligence += amount
        elif attribute.lower() is 'wisdom':
            self.wisdom += amount
        elif attribute.lower() is 'charisma':
            self.charisma += amount
    def remove_points(self, amount, attribute):
        if attribute.lower() is 'strength':
            self.strength -= amount
        elif attribute.lower() is 'dexterity':
            self.dexterity -= amount
        elif attribute.lower() is 'constitution':
            self.constitution -= amount
        elif attribute.lower() is 'intelligence':
            self.intelligence -= amount
        elif attribute.lower() is 'wisdom':
            self.wisdom -= amount
        elif attribute.lower() is 'charisma':
            self.charisma -= amount
    def clear_points(self, attribute):
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.health = 40
        self.points = 20


    def change_name(self):
        new_name = input("Please a new name: ")
        self.name = new_name



if __name__ == '__main__':
    bob = Character()

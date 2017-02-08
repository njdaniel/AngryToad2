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
        print("Creating character...")
        get_name = input("Please enter name: ")
        print("You have %d points to spend on Attributes:" % (self.points))



        # Distributing the points
        while True:
            CHARACTER_POINTS_COMMANDS = ['add_points', 'remove_points', 'clear_points']
            self._attributes = {'Strength': self.strength, 'Dexterity': self.dexterity,
                                'Constitution': self.constitution,
                                'Intelligence': self.intelligence, 'Wisdom': self.wisdom, 'Charisma': self.charisma}
            self.print_attributes()

            command = input("Enter command to alter points"
                            "(ex. <add,remove>, <attribute>, <amount>"
                            "OR <clear> to reset attributes "
                            "OR <confirm> to finalize character: ")
            numbers_inlist = [x for x in command if x.isdigit()]
            amount = int(''.join(numbers_inlist))
            attribute_to_alter = ''
            for key in self._attributes.items():
                if key[0].lower() in command:
                    attribute_to_alter = key[0].lower()
            if 'clear' in command.lower() :
                self.clear_points()
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

    # Methods to alter points
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

    def remove_points(self, amount, attribute):
        if attribute.lower() is 'strength':
            self.strength -= amount
            self.points += amount
        elif attribute.lower() is 'dexterity':
            self.dexterity -= amount
            self.points += amount
        elif attribute.lower() is 'constitution':
            self.constitution -= amount
            self.points += amount
        elif attribute.lower() is 'intelligence':
            self.intelligence -= amount
            self.points += amount
        elif attribute.lower() is 'wisdom':
            self.wisdom -= amount
            self.points += amount
        elif attribute.lower() is 'charisma':
            self.charisma -= amount
            self.points += amount

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

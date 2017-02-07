"""Character information

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
        _attributes = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
        print("Creating character...")
        get_name = input("Please enter name:")
        print("You have {points} points to spend on Attributes({attributes})").format(points=self.points,
                                                                                      attributes=_attributes)
    def change_name(self):
        new_name = input("Please a new name: ")
        self.name = new_name



if __name__ == '__main__':
    bob = Character()

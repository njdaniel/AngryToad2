from unittest.mock import patch
from unittest import TestCase

from .character import Character


class TestCharacter(TestCase):
# ------- Adding Points to Attributes ---------
    def test_add_points_to_strength(self):
        test_character = Character()
        amount = 1
        points_left = test_character.points - amount
        test_character.add_points(amount, 'Strength')
        self.assertEqual(test_character.strength, amount)
        self.assertEqual(test_character.points, points_left)

    def test_add_points_to_dexterity(self):
        test_character = Character()
        amount = 1
        points_left = test_character.points - amount
        test_character.add_points(amount, 'dexterity')
        self.assertEqual(test_character.dexterity, amount)
        self.assertEqual(test_character.points, points_left)

    def test_add_points_to_constitution(self):
        test_character = Character()
        amount = 1
        points_left = test_character.points - amount
        test_character.add_points(amount, 'constitution')
        self.assertEqual(test_character.constitution, amount)
        self.assertEqual(test_character.points, points_left)

    def test_add_points_to_intelligence(self):
        test_character = Character()
        amount = 1
        points_left = test_character.points - amount
        test_character.add_points(amount, 'intelligence')
        self.assertEqual(test_character.intelligence, amount)
        self.assertEqual(test_character.points, points_left)

    def test_add_points_to_wisdom(self):
        test_character = Character()
        amount = 1
        points_left = test_character.points - amount
        test_character.add_points(amount, 'wisdom')
        self.assertEqual(test_character.wisdom, amount)
        self.assertEqual(test_character.points, points_left)

    def test_add_points_to_charisma(self):
        test_character = Character()
        amount = 1
        points_left = test_character.points - amount
        test_character.add_points(amount, 'charisma')
        self.assertEqual(test_character.charisma, amount)
        self.assertEqual(test_character.points, points_left)


# ---------- Deleting Points from Attributes ---------------
    def test_remove_points_to_strength(self):
        test_character = Character()
        amount_to_add = 2
        amount_to_remove = 1
        amount_final = amount_to_add - amount_to_remove
        points_left = test_character.points - amount_final
        test_character.add_points(amount_to_add, 'strength')
        test_character.remove_points(amount_to_remove, 'Strength')
        self.assertEqual(test_character.strength, 1)
        self.assertEqual(test_character.points, points_left)

    def test_remove_points_to_dexterity(self):
        test_character = Character()
        amount_to_add = 2
        amount_to_remove = 1
        amount_final = amount_to_add - amount_to_remove
        points_left = test_character.points - amount_final
        test_character.add_points(amount_to_add, 'dexterity')
        test_character.remove_points(amount_to_remove, 'dexterity')
        self.assertEqual(test_character.dexterity, 1)
        self.assertEqual(test_character.points, points_left)

    def test_remove_points_to_constitution(self):
        test_character = Character()
        amount_to_add = 2
        amount_to_remove = 1
        amount_final = amount_to_add - amount_to_remove
        points_left = test_character.points - amount_final
        test_character.add_points(amount_to_add, 'constitution')
        test_character.remove_points(amount_to_remove, 'constitution')
        self.assertEqual(test_character.constitution, 1)
        self.assertEqual(test_character.points, points_left)

    def test_remove_points_to_intelligence(self):
        test_character = Character()
        amount_to_add = 2
        amount_to_remove = 1
        amount_final = amount_to_add - amount_to_remove
        points_left = test_character.points - amount_final
        test_character.add_points(amount_to_add, 'intelligence')
        test_character.remove_points(amount_to_remove, 'intelligence')
        self.assertEqual(test_character.intelligence, 1)
        self.assertEqual(test_character.points, points_left)

    def test_remove_points_to_wisdom(self):
        test_character = Character()
        amount_to_add = 2
        amount_to_remove = 1
        amount_final = amount_to_add - amount_to_remove
        points_left = test_character.points - amount_final
        test_character.add_points(amount_to_add, 'wisdom')
        test_character.remove_points(amount_to_remove, 'wisdom')
        self.assertEqual(test_character.wisdom, 1)
        self.assertEqual(test_character.points, points_left)

    def test_remove_points_to_charisma(self):
        test_character = Character()
        amount_to_add = 2
        amount_to_remove = 1
        amount_final = amount_to_add - amount_to_remove
        points_left = test_character.points - amount_final
        test_character.add_points(amount_to_add, 'charisma')
        test_character.remove_points(amount_to_remove, 'charisma')
        self.assertEqual(test_character.charisma, 1)
        self.assertEqual(test_character.points, points_left)


# ----- Points Errors -------
    def test_add_points_not_enough_strength(self):
        test_character = Character()
        amount_to_add = test_character.points + 1
        amount_should_be = test_character.points
        test_character.add_points(amount_to_add, 'strength')
        self.assertEqual(test_character.strength, amount_should_be)


    def test_remove_points_too_much_strength(self):
        test_character = Character()
        test_character.add_points(test_character.points, 'strength')
        amount_to_remove = test_character.strength + 1
        amount_should_remove = test_character.strength
        test_character.remove_points(amount_to_remove, 'strength')
        self.assertEqual(test_character.strength, 0)
        self.assertEqual(test_character.points, amount_should_remove)

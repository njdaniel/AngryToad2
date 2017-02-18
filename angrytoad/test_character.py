from unittest.mock import patch
from unittest import TestCase

from .character import Character


class TestCharacter(TestCase):
    def test_add_points_to_strength(self):
        test_character = Character()
        list_of_amounts = [x for x in test_character.points]
        test_character.__delete__
        for amount in list_of_amounts:
            test_character = Character()
            test_character.add_points(amount, 'Strength')
            self.assertEqual(test_character.strength, amount)

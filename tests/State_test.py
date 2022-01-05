import unittest

from src.Animal.Animals import *
from src.State import getAnimalState


class StateTests(unittest.TestCase):
    def test_animal_state(self):
        a = Ant()
        state = getAnimalState(a)
        self.assertEqual(len(state), 83)
        self.assertEqual(state[1], 1)
        self.assertEqual(state[-1], 1)
        self.assertEqual(state[-2], 1)
        self.assertEqual(state[-3], 1)
        self.assertEqual(state[-4], 2)

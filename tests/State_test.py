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

        state = a.getState()
        self.assertEqual(len(state), 83)
        self.assertEqual(state[1], 1)
        self.assertEqual(state[-1], 1)
        self.assertEqual(state[-2], 1)
        self.assertEqual(state[-3], 1)
        self.assertEqual(state[-4], 2)

    def test_noneanimal(self):
        a = NoneAnimal()
        state = a.getState()
        self.assertEqual(state[0], 1)
        for i in state[1:]:
            self.assertEqual(i, 0)

import unittest

from src.Animal.Animals import *
from src.State import getAnimalState
from src.Team import Team


class StateTests(unittest.TestCase):
    def test_animal_state(self):
        a = Ant()
        state = getAnimalState(a)
        self.assertEqual(len(state), 83)

        state = a.getState()
        self.assertEqual(len(state), 83)

    def test_noneanimal(self):
        a = NoneAnimal()
        state = a.getState()

    def test_team_state(self):
        t = Team()
        state = t.getState()
        print(len(state[0]))
        print(len(state[1]))

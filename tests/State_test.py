import unittest

from src.Animal.Animals import *
from src.State import getAnimalState
from src.Team import Team


class StateTests(unittest.TestCase):
    def test_animal_state(self):
        a = Ant()
        state = getAnimalState(a)
        # self.assertEqual(len(state), 84)

        state = a.getState()
        # self.assertEqual(len(state), 84)

    def test_noneanimal(self):
        a = NoneAnimal()
        state = a.getState()

    def test_team_state(self):
        t = Team()
        state = t.getState()
        print(len(state[0]))
        print(len(state[1]))

    def test_can_buy(self):
        t = Team()
        t.friends[0] = Ant()
        t.friends[1] = Ant()
        t.friends[2] = Ant()
        t.friends[3] = Ant()
        t.friends[4] = NoneAnimal()

        t.shop.animals[0] = Fish()
        t.shop.animals[1] = Fish()
        t.shop.animals[2] = NoneAnimal()

        state = t.getState()

        print(state[1][36])
        print(state[1][37])
        print(state[1][38])
        print(state[1][39])
        print(state[1][40])
        print(state[1][26:51])

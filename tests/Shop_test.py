import unittest
from src.Animal.Animals import Ant
from src.Food.Foods import CannedFood, Salad

from src.Shop import Shop
from src.Team import Team


class TeamTests(unittest.TestCase):
    def test_create(self):
        s = Shop()

        self.assertEqual(s.__class__, Shop)

    def test_shop_can(self):
        t = Team()
        f = CannedFood()
        t.shop.items[0] = f
        t.buyFood(0, 0)

        self.assertEqual(t.shop.health_modifier, 0)
        self.assertEqual(t.shop.dmg_modifier, 0)

    def test_shop_randomfood(self):
        t = Team()
        f = Salad()
        t.shop.items[0] = f
        t.friends[0] = Ant()
        t.friends[1] = Ant()

        t.buyFood(0, 0)

        self.assertEqual(t.friends[0].getHp(), 2)
        self.assertEqual(t.friends[1].getHp(), 2)

        t = Team()
        f = Salad()
        t.shop.items[0] = f
        t.friends[0] = Ant()

        t.buyFood(0, 0)

        self.assertEqual(t.friends[0].getHp(), 2)

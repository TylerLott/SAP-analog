import unittest
from src.Food.Foods import CannedFood

from src.Shop import Shop
from src.Team import Team


class TeamTests(unittest.TestCase):
    def test_create(self):
        s = Shop()

    def test_shop_can(self):
        t = Team()
        f = CannedFood()
        t.shop.items[0] = f
        t.buyFood(0, 0)

        self.assertEqual(t.shop.health_modifier, 1)
        self.assertEqual(t.shop.dmg_modifier, 1)
        print(t.shop)

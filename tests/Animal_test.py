import unittest
from src.Animal.Animals import Ant, Scorpion
from src.Food.Foods import *


class AnimalTests(unittest.TestCase):
    def test_create(self):
        an = Ant()
        self.assertEqual(an.__str__(), Ant().__str__())

    def test_set_base_hp(self):
        an = Ant()
        an.setBaseHp(10)

        self.assertEqual(an.getBaseHp(), 10)

    def test_set_temp_hp(self):
        an = Ant()
        an.setTempHp(10)

        self.assertEqual(an.getTempHp(), 10)

    def test_set_base_dmg(self):
        an = Ant()
        an.setBaseDmg(10)

        self.assertEqual(an.getBaseDmg(), 10)

    def test_set_temp_dmg(self):
        an = Ant()
        an.setTempDmg(10)

        self.assertEqual(an.getTempDmg(), 10)

    def test_get_level(self):
        an = Ant()

        self.assertEqual(an.getLevel(), 1)

        food = Chocolate()

        an += food
        an += food
        self.assertEqual(an.getLevel(), 2)

        an += food
        an += food
        an += food
        self.assertEqual(an.getLevel(), 3)

    def test_get_exp(self):
        an = Ant()

        self.assertEqual(an.getExp(), 1)

        food = Chocolate()

        an += food
        self.assertEqual(an.getExp(), 2)

        an += food
        self.assertEqual(an.getExp(), 3)

    def test_get_cost(self):
        an = Ant()
        self.assertEqual(an.getCost(), 3)

    def test_get_effect(self):
        an = Scorpion()
        self.assertEqual(an.effect, "poison")

    def test_get_state(self):
        pass

    def test_combine(self):
        an = Ant()
        an2 = Ant()
        an += an2

        self.assertEqual(an.getExp(), 2)

    ### Food Tests ###

    def test_apple(self):
        an = Ant()
        food = Apple()
        an += food

        an2 = Ant(health=1, dmg=1)
        self.assertEqual(an.__str__(), an2.__str__())

    def test_honey(self):
        pass

    def test_cupcake(self):
        an = Ant()
        food = Cupcake()
        an += food

        self.assertEqual(an.getTempDmg(), 3)
        self.assertEqual(an.getTempHp(), 3)

    def test_meat(self):
        an = Ant()
        food = MeatBone()
        an += food

        self.assertEqual(an.effect, "meat")
        # TODO test hitting

    def test_pill(self):
        # TODO write this
        pass

    def test_garlic(self):
        an = Ant()
        food = Garlic()
        an += food

        self.assertEqual(an.effect, "garlic")
        # TODO test getting hit

    def test_pear(self):
        an = Ant()
        food = Pear()
        an += food

        an2 = Ant(2, 2)
        self.assertEqual(an.__str__(), an2.__str__())

    def test_chili(self):
        an = Ant()
        food = Chili()
        an += food

        self.assertEqual(an.effect, "splash")
        # TODO test hitting

    def test_chocolate(self):
        an = Ant()
        food = Chocolate()
        an += food

        self.assertEqual(an.getExp(), 2)

    def test_melon(self):
        an = Ant()
        food = Melon()
        an += food

        self.assertEqual(an.effect, "melon")
        # TODO test getting hit

    def test_mush(self):
        an = Ant()
        food = Mushroom()
        an += food

        self.assertEqual(an.effect, "extraLife")
        # TODO test fainting

    def test_steak(self):
        an = Ant()
        food = Steak()
        an += food

        self.assertEqual(an.effect, "steak")
        # TODO test hitting

    def test_milk(self):
        an = Ant()
        food = Milk(1)
        an += food

        an2 = Ant(2, 1)
        self.assertEqual(an.__str__(), an2.__str__())

        an = Ant()
        food = Milk(2)
        an += food

        an2 = Ant(4, 2)
        self.assertEqual(an.__str__(), an2.__str__())

        an = Ant()
        food = Milk(3)
        an += food

        an2 = Ant(6, 3)
        self.assertEqual(an.__str__(), an2.__str__())

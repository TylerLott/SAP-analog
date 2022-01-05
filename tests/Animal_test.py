import unittest
from src.Animal.Animals import *
from src.Food.Foods import *
from src.Team import Team


class AnimalTests(unittest.TestCase):

    ### All Animal methods Tests ###

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
        t = Team()
        t.forceAddAnimal(0, Ant())
        food = Honey()
        t.friends[0] += food

        t.friends[0].onFaint(t.friends, t.friends)

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
        t = Team()
        t.friends[0] = Ant()
        t.shop.items[0] = Pill()
        t.buyFood(0, 0)

        self.assertFalse(t.friends[0])

    def test_garlic(self):
        an = Ant(10)
        food = Garlic()
        an += food

        self.assertEqual(an.effect, "garlic")
        an.subHp(3, [], [])
        self.assertEqual(an.getHp(), 10)

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
        an.subHp(20, [], [])
        self.assertEqual(an.getHp(), 1)

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

    ### Specific Animal Tests ###

    def test_ant(self):
        t = Team()
        t.friends[0] = Ant()
        t.friends[1] = Ant()
        t.shop.items[0] = Pill()
        t.buyFood(0, 0)

        self.assertEqual(t.friends[1].getHp(), 2)
        self.assertEqual(t.friends[1].getDmg(), 4)

    def test_badger(self):
        t = Team()
        t.friends[0] = Badger()
        t.friends[1] = Ant()

        t2 = Team()
        t2.friends[0] = Ant()

        t.friends[0].onFaint(t.friends, t2.friends)
        self.assertFalse(t.friends[1].alive)
        self.assertFalse(t2.friends[0].alive)

        t = Team()
        t.friends[0] = Ant()
        t.friends[1] = Badger()
        t.friends[2] = Ant()

        t2 = Team()
        t2.friends[0] = Ant()

        t.friends[1].onFaint(t.friends, t2.friends)
        self.assertFalse(t.friends[0].alive)
        self.assertFalse(t.friends[2].alive)
        self.assertTrue(t2.friends[0].alive)

    def test_beaver(self):
        t = Team()
        t.friends[0] = Beaver()
        t.friends[1] = Ant()

        t.sellFriend(0)

        self.assertEqual(t.friends[1].getHp(), 2)

    def test_bison(self):
        t = Team()
        t.friends[0] = Bison()
        t.friends[1] = Ant()
        for i in range(6):
            t.friends[1] += Ant()

        self.assertEqual(t.friends[1].getLevel(), 3)
        t.endTurn()
        self.assertEqual(t.friends[0].getHp(), 8)
        self.assertEqual(t.friends[0].getDmg(), 8)

    def test_blowfish(self):
        t = Team()
        t.friends[0] = Blowfish()

        t2 = Team()
        t2.friends[0] = Ant()

        t2.friends[0].attack(t2.friends, t.friends)

        self.assertFalse(t2.friends[0].alive)

    def test_boar(self):
        t = Team()
        t.friends[0] = Boar()

        t2 = Team()
        t2.friends[0] = Ant()

        t.friends[0].attack(t.friends, t2.friends)
        self.assertEqual(t.friends[0].getHp(), 8)
        self.assertEqual(t.friends[0].getDmg(), 10)

    def test_camel(self):
        t = Team()
        t.friends[0] = Camel()
        t.friends[1] = Ant()

        t2 = Team()
        t2.friends[0] = Ant()

        t2.friends[0].attack(t2.friends, t.friends)
        self.assertEqual(t.friends[1].getHp(), 3)
        self.assertEqual(t.friends[1].getDmg(), 3)

    def test_cat(self):
        t = Team()
        t.friends[0] = Ant()
        t.friends[1] = Cat()
        t.shop.items[0] = Apple()
        t.buyFood(0, 0)
        self.assertEqual(t.friends[0].getHp(), 3)
        self.assertEqual(t.friends[0].getDmg(), 4)

    def test_cow(self):
        t = Team()
        for i in range(10):
            t.nextTurn()
        t.shop.animals[0] = Cow()
        t.buyFriend(0, 0)

        self.assertEqual(t.shop.items[0].__class__, Milk)
        self.assertEqual(t.shop.items[1].__class__, Milk)

    def test_crab(self):
        t = Team()
        t.friends[0] = Bison()
        t.shop.animals[0] = Crab()
        t.buyFriend(0, 1)

        self.assertEqual(t.friends[0].getHp(), t.friends[1].getHp())

    def test_cricket(self):
        t = Team()
        t.friends[0] = Cricket()
        t.friends[0].onFaint(t.friends, [])
        self.assertEqual(t.friends[0].__class__, CricketSpawn)

    def test_crocodile(self):
        t = Team()
        t.friends[0] = Crocodile()

        t2 = Team()
        t2.friends[0] = Ant()
        t2.friends[1] = Ant()
        t2.friends[2] = Ant()
        t2.friends[3] = Ant()
        t2.friends[4] = Ant()

        t.friends[0].onStartOfBattle(t.friends, t2.friends)
        self.assertFalse(t2.friends[4].alive)

    def test_deer(self):
        t = Team()
        t.friends[0] = Deer()
        t.friends[0].onFaint(t.friends, [])

        self.assertEqual(t.friends[0].__class__, Bus)

        t2 = Team()
        t2.friends[0] = Ant()
        t2.friends[1] = Ant()

        t.friends[0].attack(t.friends, t2.friends)

        self.assertFalse(t2.friends[0].alive)
        self.assertFalse(t2.friends[1].alive)

    def test_dodo(self):
        t = Team()
        t.friends[0] = Ant()
        t.friends[1] = Dodo()

        t.friends[1].onStartOfBattle(t.friends, [])
        self.assertEqual(t.friends[0].getDmg(), 3)

    def test_dog(self):
        t = Team()
        t.friends[0] = Dog()
        t.shop.animals[0] = Ant()
        t.buyFriend(0, 1)

        self.assertEqual(t.friends[0].getDmg(), 3)
        self.assertEqual(t.friends[0].getHp(), 3)

    def test_dolphin(self):
        t = Team()
        t.friends[0] = Dolphin()

        t2 = Team()
        t2.friends[0] = Ant()
        t2.friends[2] = Bison()

        t.friends[0].onStartOfBattle(t.friends, t2.friends)
        self.assertFalse(t2.friends[0].alive)

    def test_dragon(self):
        t = Team()
        t.friends[0] = Dragon()
        t.shop.animals[0] = Ant()
        t.buyFriend(0, 1)
        self.assertEqual(t.friends[0].getHp(), 9)

    def test_duck(self):
        t = Team()
        t.friends[0] = Duck()

        t.shop.animals[0] = Ant()
        t.sellFriend(0)
        self.assertEqual(t.shop.animals[0].getHp(), 2)

    def test_elephant(self):
        t = Team()
        t.friends[0] = Elephant()
        t.friends[1] = Ant()

        t.friends[0].onBeforeAttack(t.friends, [])
        self.assertFalse(t.friends[1].alive)

    def test_fish(self):
        t = Team()
        t.friends[0] = Fish()
        t.friends[1] = Ant()
        t.friends[2] = Ant()

        t.friends[0].onLevelUp(t.friends)

        self.assertEqual(t.friends[1].getHp(), 2)
        self.assertEqual(t.friends[2].getHp(), 2)
        pass

    def test_flamingo(self):
        t = Team()
        t.friends[0] = Flamingo()
        t.friends[1] = Ant()
        t.friends[2] = Ant()

        t.friends[0].onFaint(t.friends, [])

        self.assertEqual(t.friends[1].getHp(), 2)
        self.assertEqual(t.friends[2].getHp(), 2)

    def test_fly(self):
        t = [Ant(), Fly()]
        t[1].onFriendFaint(t[0], t)

        self.assertEqual(t[0].__class__, FlySpawn)

    def test_giraffe(self):
        t = Team()
        t.friends[0] = Ant()
        t.friends[1] = Giraffe()

        t.friends[1].onEndOfTurn(t.friends)
        self.assertEqual(t.friends[0].getHp(), 2)

    def test_gorilla(self):
        t = Team()
        t.friends[0] = Gorilla()

        t2 = Team()
        t2.friends[0] = Ant(100, 0)

        t2.friends[0].attack(t2.friends, t.friends)
        self.assertEqual(t.friends[0].getHp(), 7)
        self.assertEqual(t.friends[0].effect, "coconut")

        t2.friends[0].attack(t2.friends, t.friends)
        self.assertEqual(t.friends[0].getHp(), 7)
        self.assertEqual(t.friends[0].effect, None)

    def test_hedgehog(self):
        t = Team()
        t.friends[0] = Hedgehog()
        t.friends[1] = Ant()
        t.friends[2] = Ant()

        t2 = Team()
        t2.friends[0] = Ant()
        t2.friends[1] = Ant()

        t.friends[0].onFaint(t.friends, t2.friends)
        self.assertFalse(t.friends[1].alive)
        self.assertFalse(t.friends[2].alive)
        self.assertFalse(t2.friends[0].alive)
        self.assertFalse(t2.friends[1].alive)

    def test_hippo(self):
        t = Team()
        t.friends[0] = Hippo()

        t2 = Team()
        t2.friends[0] = Ant()

        t.friends[0].attack(t.friends, t2.friends)
        self.assertEqual(t.friends[0].getHp(), 9)

    def test_horse(self):
        t = Team()
        t.friends[4] = Horse()
        t.shop.animals[0] = Ant()
        t.buyFriend(0, 0)

        self.assertEqual(t.friends[0].getTempDmg(), 1)

    def test_kangaroo(self):
        t = Team()
        t.friends[0] = Ant(10, 0)
        t.friends[1] = Kangaroo()

        t2 = Team()
        t2.friends[0] = Ant()

        t.friends[0].attack(t.friends, t2.friends)

        self.assertEqual(t.friends[1].getHp(), 4)

    def test_leopard(self):
        t = Team()
        t.friends[0] = Leopard()

        t2 = Team()
        t2.friends[0] = Ant()

        t.friends[0].onStartOfBattle(t.friends, t2.friends)
        self.assertFalse(t2.friends[0].alive)

    def test_mammoth(self):
        t = Team()
        t.friends[0] = Mammoth()
        t.friends[1] = Ant()
        t.friends[2] = Ant()

        t.friends[0].onFaint(t.friends, [])
        self.assertEqual(t.friends[1].getHp(), 3)
        self.assertEqual(t.friends[2].getHp(), 3)

    def test_mosquito(self):
        t = Team()
        t.friends[0] = Mosquito()

        t2 = Team()
        t2.friends[0] = Ant()

        t.friends[0].onStartOfBattle(t.friends, t2.friends)
        self.assertFalse(t2.friends[0].alive)

    def test_monkey(self):
        t = Team()
        t.friends[0] = Ant()
        t.friends[1] = Monkey()

        t.friends[1].onEndOfTurn(t.friends)
        self.assertEqual(t.friends[0].getHp(), 4)

    def test_otter(self):
        t = Team()
        t.friends[0] = Ant()

        t.shop.animals[0] = Otter()
        t.buyFriend(0, 1)

        self.assertEqual(t.friends[0].getHp(), 2)

        t.shop.animals[0] = Otter()
        t.buyFriend(0, 1)
        t.shop.animals[0] = Otter()
        t.buyFriend(0, 1)

        self.assertEqual(t.friends[0].getHp(), 5)

    def test_ox(self):
        t = Team()
        t.friends[0] = Ant()
        t.friends[1] = Ox()

        self.assertEqual(t.friends[1].effect, None)

        t.friends[1].onFriendAheadFaint(t.friends, [])

        self.assertEqual(t.friends[1].effect, "melon")
        self.assertEqual(t.friends[1].getDmg(), 3)

    def test_parrot(self):
        t = Team()
        t.friends[0] = Ant()
        t.friends[1] = Parrot()

        t.friends[1].onStartOfBattle(t.friends, [])
        self.assertEqual(t.friends[1].__class__, Ant)
        self.assertEqual(t.friends[1].getHp(), 3)
        self.assertEqual(t.friends[1].getDmg(), 5)

    def test_peacock(self):
        t = Team()
        t.friends[0] = Peacock()
        t.friends[0].subHp(1, t.friends, [])

        self.assertEqual(t.friends[0].getDmg(), 3)

    def test_penguin(self):
        t = Team()
        t.friends[0] = Ant()
        for i in range(2):
            t.friends[0] += Ant()
        t.friends[1] = Penguin()
        t.friends[1].onEndOfTurn(t.friends)

        self.assertEqual(t.friends[0].getHp(), 4)

    def test_pig(self):
        t = Team()
        t.friends[0] = Pig()
        t.sellFriend(0)
        self.assertEqual(t.getMoney(), 12)

    def test_rabbit(self):
        t = Team()
        t.friends[0] = Rabbit()
        t.friends[1] = Ant()
        t.shop.items[0] = Apple()
        t.buyFood(0, 1)

        self.assertEqual(t.friends[1].getHp(), 3)

    def test_rat(self):
        t = Team()
        t.friends[0] = Rat()
        t2 = [Ant()]
        t.friends[0].onFaint(t.friends, t2)

        self.assertEqual(t2[1].__class__, DirtyRat)

    def test_rhino(self):
        t = Team()
        t.friends[0] = Rhino()

        t2 = Team()
        t2.friends[0] = Ant()
        t2.friends[1] = Ant()

        t.friends[0].attack(t.friends, t2.friends)
        self.assertFalse(t2.friends[0].alive)
        self.assertFalse(t2.friends[1].alive)

    def test_rooster(self):
        t = Team()
        t.friends[0] = Rooster()
        t.friends[0].onFaint(t.friends, [])
        self.assertEqual(t.friends[0].__class__, Chick)

    def test_scorpion(self):
        t = Team()
        t.friends[0] = Scorpion()

        t2 = Team()
        t2.friends[0] = Ant(100, 0)

        t.friends[0].attack(t.friends, t2.friends)
        self.assertFalse(t2.friends[0].alive)

    def test_seal(self):
        t = Team()
        t.friends[0] = Seal()
        t.friends[1] = Ant()
        t.friends[2] = Ant()
        t.shop.items[0] = Apple()

        t.buyFood(0, 0)

        self.assertEqual(t.friends[1].getHp(), 2)
        self.assertEqual(t.friends[2].getHp(), 2)

    def test_shark(self):
        t = Team()
        t.friends[0] = Shark()

        t.friends[0].onFriendFaint(Ant(), t.friends)

        self.assertEqual(t.friends[0].getHp(), 5)

    def test_sheep(self):
        # did this because noneanimals, kinda jank
        t = [Sheep()]

        t[0].onFaint(t, [])

        self.assertEqual(t[0].__class__, Ram)
        self.assertEqual(t[1].__class__, Ram)

    def test_shrimp(self):
        t = Team()
        t.friends[0] = Shrimp()
        t.friends[1] = Ant()
        t.friends[2] = Ant()
        t.sellFriend(2)

        self.assertEqual(t.friends[1].getHp(), 2)

    def test_skunk(self):
        t = Team()
        t.friends[0] = Skunk()

        t2 = Team()
        t2.friends[0] = Ant(2)

        t.friends[0].onStartOfBattle(t.friends, t2.friends)

        self.assertEqual(t2.friends[0].getHp(), 1)

    def test_sloth(self):
        # nothing
        pass

    def test_snail(self):
        t = Team()
        t.friends[0] = Ant()
        t.friends[1] = Ant()
        t.wonLast = False

        t.shop.animals[0] = Snail()

        t.buyFriend(0, 2)
        self.assertEqual(t.friends[0].getHp(), 2)
        self.assertEqual(t.friends[1].getHp(), 2)

    def test_snake(self):
        t = Team()
        t.friends[0] = Snake()

        t2 = Team()
        t2.friends[0] = Ant()

        t.friends[0].onFriendAheadAttack(t.friends, t2.friends)

        self.assertFalse(t2.friends[0].alive)

    def test_spider(self):
        t = Team()
        t.friends[0] = Spider()
        t.friends[0].onFaint(t.friends, [])

        self.assertEqual(t.friends[0].tier, 3)

    def test_squirrel(self):
        t = Team()
        t.friends[0] = Squirrel()
        t.friends[0].onStartOfTurn(t)

        self.assertEqual(t.shop.items[0].cost, 2)

    def test_swan(self):
        t = Team()
        t.friends[0] = Swan()
        t.friends[0].onStartOfTurn(t)

        self.assertEqual(t.getMoney(), 11)

    def test_tiger(self):
        # TODO implement tiger
        pass

    def test_turkey(self):
        t = Team()
        t.friends[0] = Spider()
        t.friends[1] = Turkey()

        t.friends[0].onFaint(t.friends, [])
        self.assertNotEqual(t.friends[0].__class__, Spider)

    def test_turtle(self):
        t = Team()
        t.friends[0] = Turtle()
        t.friends[1] = Ant()

        t.friends[0].onFaint(t.friends, [])
        self.assertEqual(t.friends[1].effect, "melon")

    def test_whale(self):
        t = Team()
        t.friends[0] = Sloth()
        t.friends[1] = Whale()

        t.friends[1].onStartOfBattle(t.friends, [])
        self.assertEqual(t.friends[1].jonah.__class__, Sloth)

        t.friends[1].onFaint(t.friends, [])
        self.assertEqual(t.friends[1].__class__, Sloth)

    def test_worm(self):
        t = Team()
        t.friends[0] = Worm()
        t.shop.items[0] = Apple()
        t.buyFood(0, 0)
        self.assertEqual(t.friends[0].getHp(), 4)
        self.assertEqual(t.friends[0].getDmg(), 4)

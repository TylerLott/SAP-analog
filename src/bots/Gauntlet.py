from src.Team import Team
from src.Animal.Animals import *
import random

# Custom Curated Teams
def getGauntlet(round: int = 1) -> Team:
    if round == 1:
        t1 = Team()
        t1.friends[0] = Ant()
        t1.friends[1] = Beaver(dmg=1)
        t1.friends[2] = Horse()
        t2 = Team()
        t2.friends[0] = Otter()
        t2.friends[1] = Cricket(dmg=1, health=1)
        t2.friends[2] = Horse()
        t3 = Team()
        t3.friends[0] = Ant()
        t3.friends[1] = Mosquito()
        t3.friends[2] = Mosquito()
        # t4 = Team()
        # t4.friends[2] = Horse()
        # t5 = Team()
        # t5.friends[0] = Otter()
        # t5.friends[2] = Horse()
        # t6 = Team()
        # t6.friends[0] = Ant()
        # team = random.choice([t1, t2, t3, t4, t5, t6])
        team = random.choice([t1, t2, t3])
    elif round == 2:
        t1 = Team()
        t1.friends[0] = Ant()
        t1.friends[1] = Beaver(dmg=1)
        t1.friends[2] = Beaver()
        t1.friends[3] = Mosquito(dmg=1)
        t1.friends[4] = Horse()
        t1.friends[4].effect = "honey"
        t2 = Team()
        t2.friends[0] = Beaver(dmg=2)
        t2.friends[1] = Otter(dmg=1)
        t2.friends[2] = Horse(health=1, dmg=1)
        t3 = Team()
        t3.friends[0] = Ant(dmg=2, health=1)
        t3.friends[1] = Otter()
        t3.friends[2] = Cricket(dmg=1)
        t3.friends[3] = Cricket(dmg=1, health=1)
        t3.friends[4] = Horse()

        team = random.choice([t1, t2, t3])
    elif round == 3:
        t1 = Team()
        t1.friends[0] = Ant()
        t1.friends[1] = Beaver(dmg=3, health=3)
        t1.friends[2] = Mosquito(dmg=1)
        t1.friends[3] = Horse()
        t1.friends[4] = Badger()
        t1.friends[3].effect = "honey"
        t2 = Team()
        t2.friends[0] = Spider()
        t2.friends[1] = Mosquito(health=2, dmg=2)
        t2.friends[2] = Fish(health=2)
        t2.friends[3] = Swan()
        t2.friends[4] = Swan()
        t3 = Team()
        t3.friends[0] = Ant(dmg=2, health=1)
        t3.friends[1] = Otter(dmg=1, health=1)
        t3.friends[2] = Cricket(dmg=3, health=3)
        t3.friends[3] = Rabbit(dmg=1)
        t3.friends[4] = Horse()
        t3.friends[0].exp = 3

        team = random.choice([t1, t2, t3])
    elif round == 4:
        t1 = Team()
        t1.friends[0] = Beaver(dmg=3, health=3)
        t1.friends[1] = Mosquito(dmg=1)
        t1.friends[2] = Horse()
        t1.friends[3] = Horse(dmg=1)
        t1.friends[4] = Badger(dmg=2, health=1)
        t1.friends[3].effect = "honey"
        t2 = Team()
        t2.friends[0] = Ant(dmg=2, health=2)
        t2.friends[1] = Flamingo(dmg=2, health=2)
        t2.friends[2] = Camel()
        t2.friends[3] = Cricket(dmg=1, health=1)
        t2.friends[4] = Spider()
        t2.friends[1].effect = "meat"
        t2.friends[4].effect = "honey"
        t3 = Team()
        t3.friends[0] = Ant()
        t3.friends[1] = Ant(dmg=4, health=2)
        t3.friends[2] = Otter(dmg=3, health=2)
        t3.friends[3] = Cricket(dmg=6, health=5)
        t3.friends[4] = Rabbit(dmg=3, health=1)
        t3.friends[1].exp = 3
        t3.friends[3].exp = 3

        team = random.choice([t1, t2, t3])
    elif round == 5:
        t1 = Team()
        t1.friends[0] = Beaver(dmg=4, health=4)
        t1.friends[1] = Mosquito(dmg=1)
        t1.friends[3] = Horse(dmg=3, health=2)
        t1.friends[4] = Badger(dmg=2, health=1)
        t1.friends[3].effect = "honey"
        t1.friends[4].effect = "honey"
        t2 = Team()
        t2.friends[0] = Ant(health=2, dmg=2)
        t2.friends[1] = Ox(dmg=4)
        t2.friends[2] = Blowfish(dmg=1, health=1)
        t2.friends[3] = Otter(dmg=1, health=1)
        t2.friends[4] = Badger()
        t2.friends[0].exp = 3
        t2.friends[0].effect = "meat"
        t2.friends[1].effect = "melon"
        t2.friends[2].effect = "meat"
        t3 = Team()
        t3.friends[0] = Ant(dmg=5, health=4)
        t3.friends[1] = Otter(dmg=3, health=2)
        t3.friends[2] = Cricket(dmg=6, health=5)
        t3.friends[3] = Swan(dmg=1, health=1)
        t3.friends[4] = Rabbit(dmg=3, health=1)
        t3.friends[0].exp = 3
        t3.friends[2].exp = 3
        t3.friends[0].effect = "garlic"

        team = random.choice([t1, t2, t3])
    elif round == 6:
        t1 = Team()
        t1.friends[0] = Beaver(dmg=7, health=6)
        t1.friends[1] = Mosquito(dmg=2, health=1)
        t1.friends[2] = Parrot(dmg=4, health=1)
        t1.friends[3] = Horse(dmg=4, health=3)
        t1.friends[4] = Badger(dmg=4, health=2)
        t1.friends[3].effect = "honey"
        t1.friends[4].effect = "honey"
        t2 = Team()
        t2.friends[0] = Ant(dmg=8, health=7)
        t2.friends[1] = Otter(dmg=10, health=9)
        t2.friends[2] = Giraffe(dmg=1, health=1)
        t2.friends[3] = Swan(dmg=4, health=3)
        t2.friends[4] = Fish(dmg=4, health=3)
        t2.friends[0].exp = 3
        t2.friends[1].effect = "melon"
        t3 = Team()
        t3.friends[0] = Ant(dmg=5, health=4)
        t3.friends[1] = Cricket(dmg=6, health=5)
        t3.friends[2] = Swan(dmg=3, health=7)
        t3.friends[3] = Rabbit()
        t3.friends[4] = Rabbit(dmg=4, health=4)
        t3.friends[0].exp = 3
        t3.friends[1].exp = 3
        t3.friends[0].effect = "garlic"

        team = random.choice([t1, t2, t3])
    elif round == 7:
        t1 = Team()
        t1.friends[0] = Horse(dmg=4, health=3)
        t1.friends[1] = Ox(dmg=2)
        t1.friends[2] = Parrot(dmg=4, health=3)
        t1.friends[3] = Beaver(dmg=7, health=6)
        t1.friends[4] = Badger(dmg=5, health=3)
        t1.friends[0].effect = "honey"
        t1.friends[4].effect = "honey"
        t2 = Team()
        t2.friends[0] = Hedgehog()
        t2.friends[1] = Peacock()
        t2.friends[2] = Blowfish(dmg=5, health=5)
        t2.friends[3] = Mosquito(dmg=5, health=5)
        t2.friends[4] = Swan(dmg=4, health=5)
        t2.friends[2].effect = "garlic"
        t2.friends[4].effect = "honey"
        t3 = Team()
        t3.friends[0] = Ant(dmg=5, health=4)
        t3.friends[1] = Cricket(dmg=7, health=6)
        t3.friends[2] = Ox(dmg=1, health=1)
        t3.friends[3] = Swan(dmg=3, health=7)
        t3.friends[4] = Rabbit(dmg=5, health=5)
        t3.friends[0].exp = 3
        t3.friends[1].exp = 3
        t3.friends[0].effect = "garlic"

        team = random.choice([t1, t2, t3])
    elif round == 8:
        t1 = Team()
        t1.friends[0] = Horse(dmg=4, health=3)
        t1.friends[1] = Ox()
        t1.friends[2] = Parrot(dmg=5, health=4)
        t1.friends[3] = Beaver(dmg=7, health=6)
        t1.friends[4] = Badger(dmg=5, health=3)
        t1.friends[0].exp = 3
        t1.friends[2].exp = 3
        t1.friends[0].effect = "honey"
        t1.friends[3].effect = "garlic"
        t1.friends[4].effect = "honey"
        t2 = Team()
        t2.friends[0] = Camel(dmg=10, health=18)
        t2.friends[1] = Kangaroo(dmg=2, health=1)
        t2.friends[2] = Swan(dmg=8, health=12)
        t2.friends[3] = Rabbit(dmg=4, health=5)
        t2.friends[4] = Squirrel()
        t2.friends[0].exp = 3
        t2.friends[0].effect = "garlic"
        t3 = Team()
        t3.friends[0] = Ant(dmg=5, health=4)
        t3.friends[1] = Cricket(dmg=7, health=7)
        t3.friends[2] = Ox(dmg=2, health=2)
        t3.friends[3] = Swan(dmg=3, health=8)
        t3.friends[4] = Rabbit(dmg=5, health=5)
        t3.friends[0].exp = 3
        t3.friends[1].exp = 3
        t3.friends[2].exp = 3
        t3.friends[0].effect = "garlic"
        t3.friends[1].effect = "garlic"
        t3.friends[3].effect = "garlic"

        team = random.choice([t1, t2, t3])
    elif round == 9:
        t1 = Team()
        t1.friends[0] = Scorpion()
        t1.friends[1] = Ox(dmg=2)
        t1.friends[2] = Parrot(dmg=6, health=5)
        t1.friends[3] = Beaver(dmg=7, health=6)
        t1.friends[4] = Badger(dmg=5, health=3)
        t1.friends[2].exp = 3
        t1.friends[1].effect = "melon"
        t1.friends[3].effect = "garlic"
        t1.friends[4].effect = "honey"
        t2 = Team()
        t2.friends[0] = Cricket(dmg=4, health=4)
        t2.friends[1] = Rooster(dmg=8, health=8)
        t2.friends[2] = Shark()
        t2.friends[3] = Turkey(dmg=3, health=3)
        t2.friends[4] = Turkey()
        t2.friends[0].exp = 3
        t2.friends[1].exp = 3
        t2.friends[0].effect = "meat"
        t2.friends[1].effect = "meat"
        t3 = Team()
        team = random.choice([t1, t2, t3])
    elif round == 10:
        t1 = Team()
        t1.friends[0] = Scorpion()
        t1.friends[1] = Ox(dmg=2)
        t1.friends[2] = Parrot(dmg=9, health=8)
        t1.friends[3] = Beaver(dmg=7, health=6)
        t1.friends[4] = Badger(dmg=6, health=4)
        t1.friends[2].exp = 3
        t1.friends[1].effect = "melon"
        t1.friends[3].effect = "garlic"
        t1.friends[4].effect = "honey"
        t2 = Team()
        t2.friends[0] = Otter(dmg=12, health=12)
        t2.friends[1] = Dodo(dmg=13, health=15)
        t2.friends[2] = Sheep(dmg=5, health=5)
        t2.friends[3] = Dog(dmg=8, health=9)
        t2.friends[4] = Penguin(dmg=2, health=2)
        t2.friends[1].exp = 3
        t2.friends[0].effect = "honey"
        t2.friends[2].effect = "garlic"
        t3 = Team()
        t3.friends[0] = Ant(dmg=5, health=4)
        t3.friends[1] = Cricket(dmg=10, health=12)
        t3.friends[2] = Ox(dmg=3, health=3)
        t3.friends[3] = Swan(dmg=3, health=8)
        t3.friends[4] = Rabbit(dmg=5, health=5)
        t3.friends[0].exp = 3
        t3.friends[1].exp = 3
        t3.friends[2].exp = 3
        t3.friends[0].effect = "garlic"
        t3.friends[1].effect = "garlic"
        t3.friends[3].effect = "garlic"

        team = random.choice([t1, t2, t3])
    elif round == 11:
        t1 = Team()
        t1.friends[0] = Scorpion(health=3)
        t1.friends[1] = Boar()
        t1.friends[2] = Parrot(dmg=13, health=15)
        t1.friends[3] = Beaver(dmg=7, health=6)
        t1.friends[4] = Badger(dmg=6, health=4)
        t1.friends[2].exp = 3
        t1.friends[4].effect = "honey"
        t2 = Team()
        t2.friends[0] = Cricket(dmg=4, health=4)
        t2.friends[1] = Rooster(dmg=9, health=9)
        t2.friends[2] = Turkey(dmg=5, health=5)
        t2.friends[3] = Turkey(dmg=6, health=5)
        t2.friends[4] = Shark()
        t2.friends[0].exp = 3
        t2.friends[1].exp = 3
        t2.friends[2].exp = 3
        t2.friends[0].effect = "meat"
        t2.friends[1].effect = "extraLife"
        t3 = Team()
        t3.friends[0] = Cricket(dmg=16, health=18)
        t3.friends[1] = Ox(dmg=5, health=7)
        t3.friends[2] = Swan(dmg=3, health=8)
        t3.friends[3] = Monkey()
        t3.friends[4] = Monkey()
        t3.friends[0].exp = 3
        t3.friends[1].exp = 6
        t3.friends[0].effect = "garlic"
        t3.friends[2].effect = "garlic"

        team = random.choice([t1, t2, t3])
    else:
        t1 = Team()
        t1.friends[0] = Mammoth(dmg=6, health=6)
        t1.friends[1] = Cricket(dmg=4, health=4)
        t1.friends[2] = Rooster(dmg=10, health=10)
        t1.friends[3] = Turkey(dmg=5, health=5)
        t1.friends[4] = Turkey(dmg=6, health=5)
        t1.friends[1].exp = 3
        t1.friends[2].exp = 3
        t1.friends[3].exp = 3
        t1.friends[0].effect = "steak"
        t1.friends[1].effect = "extraLife"
        t1.friends[2].effect = "extraLife"
        t2 = Team()
        t2.friends[0] = Mammoth(dmg=6, health=6)
        t2.friends[1] = Cricket(dmg=4, health=4)
        t2.friends[2] = Rooster(dmg=9, health=9)
        t2.friends[3] = Turkey(dmg=5, health=5)
        t2.friends[4] = Turkey(dmg=6, health=5)
        t2.friends[1].exp = 3
        t2.friends[2].exp = 3
        t2.friends[3].exp = 3
        t2.friends[0].effect = "steak"
        t2.friends[1].effect = "meat"
        t2.friends[2].effect = "extraLife"
        t3 = Team()
        t3.friends[0] = Cricket(dmg=24, health=30)
        t3.friends[1] = Ox(dmg=5, health=7)
        t3.friends[2] = Snake()
        t3.friends[3] = Swan(dmg=3, health=8)
        t3.friends[4] = Monkey(dmg=2, health=2)
        t3.friends[0].exp = 3
        t3.friends[1].exp = 6
        t3.friends[0].effect = "garlic"
        t3.friends[3].effect = "garlic"

        team = random.choice([t1, t2, t3])

    return team

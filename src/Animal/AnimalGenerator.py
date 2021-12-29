from random import randint
import sys
import os

sys.path.append(os.getcwd())

from src.Animal.Animals import *

animals = {
    1: [Ant, Beaver, Cricket, Duck, Fish, Horse, Mosquito, Otter, Pig],
    2: [Crab, Dodo, Elephant, Flamingo, Hedgehog, Peacock, Rat, Shrimp, Spider, Swan],
    3: [
        Badger,
        Blowfish,
        Camel,
        Dog,
        Giraffe,
        Kangaroo,
        Ox,
        Rabbit,
        Sheep,
        Snail,
        Turtle,
    ],
    4: [
        Bison,
        Deer,
        Dolphin,
        Hippo,
        Parrot,
        Penguin,
        Rooster,
        Skunk,
        Squirrel,
        Whale,
        Worm,
    ],
    5: [Cow, Crocodile, Monkey, Rhino, Scorpion, Seal, Shark, Turkey],
    6: [Boar, Cat, Dragon, Fly, Gorilla, Leopard, Mammoth, Snake, Tiger],
}


def getRandomAnimal(maxTier: int, health_mod: int = 0, dmg_mod: int = 0) -> Animal:
    if maxTier == 1:
        tier = 1
    else:
        tier = randint(1, maxTier - 1)
    animal = randint(0, len(animals[tier]) - 1)
    return animals[tier][animal](health_mod, dmg_mod, 0)


if __name__ == "__main__":
    count = 0
    for i in animals.keys():
        count += len(animals[i])

    print(count)

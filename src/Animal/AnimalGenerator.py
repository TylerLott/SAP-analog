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
    possible = []
    for i in range(1, maxTier + 1):
        possible += animals[i]
    animal = randint(0, len(possible) - 1)
    return possible[animal](health_mod, dmg_mod)


if __name__ == "__main__":
    for i in range(10):
        print(getRandomAnimal(3, 0, 0))

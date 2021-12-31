from random import randint
from src.Food.Foods import *

foods = {
    1: [Apple, Honey],
    2: [Cupcake, MeatBone, Pill],
    3: [Garlic, Salad],
    4: [CannedFood, Pear],
    5: [Chili, Chocolate, Sushi],
    6: [Melon, Mushroom, Pizza, Steak],
}


def getRandomFood(maxTier: int) -> Food:
    possible = []
    for i in range(1, maxTier + 1):
        possible += foods[i]
    food = randint(0, len(possible) - 1)
    return possible[food]()

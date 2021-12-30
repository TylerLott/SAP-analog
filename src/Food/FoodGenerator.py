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
    if maxTier == 1:
        tier = 1
    else:
        tier = randint(1, maxTier - 1)
    food = randint(0, len(foods[tier]) - 1)
    return foods[tier][food]()

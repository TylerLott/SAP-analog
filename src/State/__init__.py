import numpy as np

# The index of animal state that cooresponds to a given animal
# only includes possible animal (not dirtyrat)
# in order of appearance in animals.py
ANIMAL_STATE_DICT = {
    "NoneAnimal": 0,  # make sure if none animal, all values in array are 0 except for the first
    "Ant": 1,
    "Badger": 2,
    "Beaver": 3,
    "Bison": 4,
    "Blowfish": 5,
    "Boar": 6,
    "Camel": 7,
    "Cat": 8,
    "Cow": 9,
    "Crab": 10,
    "Cricket": 11,
    "CricketSpawn": 12,
    "Crocodile": 13,
    "Deer": 14,
    "Bus": 15,
    "Dodo": 16,
    "Dog": 17,
    "Dolphin": 18,
    "Dragon": 19,
    "Duck": 20,
    "Elephant": 21,
    "Fish": 22,
    "Flamingo": 23,
    "Fly": 24,
    "FlySpawn": 25,
    "Giraffe": 26,
    "Gorilla": 27,
    "Hedgehog": 28,
    "Hippo": 29,
    "Horse": 30,
    "Kangaroo": 31,
    "Leopard": 32,
    "Mammoth": 33,
    "Mosquito": 34,
    "Monkey": 35,
    "Otter": 36,
    "Ox": 37,
    "Parrot": 38,
    "Peacock": 39,
    "Penguin": 40,
    "Pig": 41,
    "Rabbit": 42,
    "Rat": 43,
    "Rhino": 44,
    "Rooster": 45,
    "Chick": 46,
    "Scorpion": 47,
    "Seal": 48,
    "Shark": 49,
    "Sheep": 50,
    "Ram": 51,
    "Shrimp": 52,
    "Skunk": 53,
    "Sloth": 54,
    "Snail": 55,
    "Snake": 56,
    "Spider": 57,
    "Squirrel": 58,
    "Swan": 59,
    "Tiger": 60,
    "Turkey": 61,
    "Turtle": 62,
    "Whale": 63,
    "Worm": 64,
    "Bee": 65,
}

# index of effects
# in order of Food README
ANIMAL_EFFECT_DICT = {
    "meat": 66,
    "chili": 67,
    "steak": 68,
    "poison": 69,
    "weak": 70,
    "garlic": 71,
    "melon": 72,
    "honey": 73,
    "extraLife": 74,
    "coconut": 75,
    None: 76,
}

# State Array
# [Animal, Animal effect, temp_dmg, temp_hp, perm_dmg, perm_hp, exp, level]
#   [66]        [11]         [1]      [1]       [1]       [1]   [1]    [1]

# So should be a len == 83 array for each animal in a team


def getAnimalState(animal) -> np.array:
    arr = np.zeros(83)
    if animal.__class__.__name__ == "NoneAnimal":
        arr[0] = 1
        return arr

    animal_ind = ANIMAL_STATE_DICT[animal.__class__.__name__]
    arr[animal_ind] = 1

    eff_ind = ANIMAL_EFFECT_DICT[animal.getEffect()]
    arr[eff_ind] = 1

    arr[82] = animal.getLevel()
    arr[81] = animal.getExp()
    arr[80] = animal.getBaseHp()
    arr[79] = animal.getBaseDmg()
    arr[78] = animal.getTempHp()
    arr[77] = animal.getTempDmg()

    return arr

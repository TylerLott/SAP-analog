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
    "splash": 76,
    None: 77,
}


# Food State Dict
FOOD_STATE_DICT = {
    "NoneFood": 0,
    "Apple": 1,
    "Honey": 2,
    "Cupcake": 3,
    "MeatBone": 4,
    "Pill": 5,
    "Garlic": 6,
    "Salad": 7,
    "CannedFood": 8,
    "Pear": 9,
    "Chili": 10,
    "Chocolate": 11,
    "Sushi": 12,
    "Melon": 13,
    "Mushroom": 14,
    "Pizza": 15,
    "Steak": 16,
    "Milk": 17,
}


# Animal State Array
# [Animal, Animal effect, temp_dmg, temp_hp, perm_dmg, perm_hp, exp, level]
#   [66]        [11]         [1]      [1]       [1]       [1]   [1]    [1]

# So should be a len == 83 array for each animal in a team


def getAnimalState(animal) -> np.array:
    # original (one hot)
    arr = np.zeros(84)
    if animal.__class__.__name__ == "NoneAnimal":
        arr[0] = 1
        return arr

    animal_ind = ANIMAL_STATE_DICT[animal.__class__.__name__]
    arr[animal_ind] = 1

    eff_ind = ANIMAL_EFFECT_DICT[animal.getEffect()]
    arr[eff_ind] = 1

    arr[83] = animal.getLevel() / 3
    arr[82] = animal.getExp() / 6
    arr[81] = animal.getBaseHp() / 50
    arr[80] = animal.getBaseDmg() / 50
    arr[79] = animal.getTempHp() / 50
    arr[78] = animal.getTempDmg() / 50

    # arr = np.zeros(8)
    # arr[0] = ANIMAL_STATE_DICT[animal.__class__.__name__] / 66
    # arr[1] = (ANIMAL_EFFECT_DICT[animal.getEffect()] - 66) / 12
    # arr[2] = animal.getLevel() / 3
    # arr[3] = animal.getExp() / 6
    # arr[4] = animal.getBaseHp() / 50
    # arr[5] = animal.getBaseDmg() / 50
    # arr[6] = animal.getTempHp() / 50
    # arr[7] = animal.getTempDmg() / 50

    return arr


def getFoodState(food) -> np.array:
    arr = np.zeros(18)

    food_ind = FOOD_STATE_DICT[food.__class__.__name__]
    arr[food_ind] = 1

    # arr = np.array([FOOD_STATE_DICT[food.__class__.__name__] / 18])

    return arr


def getPossibleMovesState(team):
    # Possible moves state
    # possible moves:
    #    - roll            [1]
    #    - end turn        [1]
    #    - move animals    [20]
    #    - sell animals    [5]
    #    - buy animals     [5 * 5 = 25]
    #    - buy food        [2 * 5 = 10]
    #    - freeze          [7]
    #    Total             [69]

    if team.moves > 10:
        roll = np.array([0])
        move_animals = np.zeros(20)
        sell_animals = np.zeros(5)
        buyAnimals = np.zeros(25)
        buyFood = np.zeros(10)
        freeze = np.zeros(7)
        end_turn = np.array([1])

        return (
            roll,
            move_animals,
            sell_animals,
            buyAnimals,
            buyFood,
            freeze,
            end_turn,
        )

    # able to do if money
    roll = np.array([0])
    if team.getMoney() > 0:
        roll[0] = 1

    # able to do if empty, or the same animal
    # i x j (4 x 5)
    # [[0 -> 1], [0 -> 2], [0 -> 3], [0 -> 4],
    #  [1 -> 0], [1 -> 2], [1 -> 3], [1 -> 4],
    #  [2 -> 0], [2 -> 1], [2 -> 3], [2 -> 4],
    #  [3 -> 0], [3 -> 1], [3 -> 2], [3 -> 4],
    #  [4 -> 0], [4 -> 1], [4 -> 2], [4 -> 3]]
    move_animals = np.zeros(shape=(5, 4))
    for i in range(len(team.friends)):
        for j in range(len(team.friends)):
            if i == j:
                continue
            if (
                (
                    team.friends[i]
                    and team.friends[j].__class__ == team.friends[i].__class__
                )
                or (team.friends[i] and not team.friends[j])
                or (team.friends[i] and not team.friends[j])
            ):
                col = j if j < i else j - 1
                move_animals[i][col] = 1
    move_animals = move_animals.flatten()

    # able to do if have animal
    # [0, 1, 2, 3, 4]
    sell_animals = np.zeros(5)
    for i in range(len(team.friends)):
        if team.friends[i]:
            sell_animals[i] = 1

    # able to do if same animal or empty
    # i x j (5x5)
    # [s0 -> 0], [s0 -> 1], [s0 -> 2], [s0 -> 3], [s0 -> 4]
    # [s1 -> 0], [s1 -> 1], [s1 -> 2], [s1 -> 3], [s1 -> 4]
    # [s2 -> 0], [s2 -> 1], [s2 -> 2], [s2 -> 3], [s2 -> 4]
    # [s3 -> 0], [s3 -> 1], [s3 -> 2], [s3 -> 3], [s3 -> 4]
    # [s4 -> 0], [s4 -> 1], [s4 -> 2], [s4 -> 3], [s4 -> 4]
    buyAnimals = np.zeros(shape=(5, 5))
    if team.getMoney() >= 3:
        for i in range(len(team.shop.animals)):
            if team.shop.animals[i]:
                for j in range(len(team.friends)):
                    if (
                        team.friends[j].__class__ == team.shop.animals[i].__class__
                        or not team.friends[j]
                    ):
                        buyAnimals[i][j] = 1
    buyAnimals = buyAnimals.flatten()

    # should always be able to do any of these
    # [s0 -> 0], [s0 -> 1], [s0 -> 2], [s0 -> 3], [s0 -> 4]
    # [s1 -> 0], [s1 -> 1], [s1 -> 2], [s1 -> 3], [s1 -> 4]
    buyFood = np.zeros(shape=(2, 5))
    for i in range(len(team.shop.items)):
        for j in range(len(team.friends)):
            if (
                (
                    team.friends[j]
                    or team.shop.items[i].__class__.__name__
                    in [
                        "CannedFood",
                        "Salad",
                        "Sushi",
                        "Pizza",
                    ]
                )
                and team.getMoney() >= team.shop.items[i].cost
                and team.shop.items[i]
            ):
                buyFood[i][j] = 1
    buyFood = buyFood.flatten()

    # [[friends], [shop]]
    # [0,1,2,3,4,5,6]
    freeze = np.zeros(7)
    can_freeze = False
    for i in team.friends:
        if i:
            can_freeze = True
    if can_freeze:
        for i in range(len(team.shop.animals)):
            if team.shop.animals[i]:
                freeze[i] = 1
        for i in range(len(team.shop.items)):
            if team.shop.items[i]:
                freeze[i + 5] = 1

    # always able to do
    end_turn = np.array([0]) if team.money > 0 else np.array([1])
    # end_turn = np.array([1])

    return (
        roll,
        move_animals,
        sell_animals,
        buyAnimals,
        buyFood,
        freeze,
        end_turn,
    )

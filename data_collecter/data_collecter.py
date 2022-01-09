import csv


s = """
############################################
 __        __   _                          
 \ \      / /__| | ___ ___  _ __ ___   ___ 
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \
   \ V  V /  __/ | (_| (_) | | | | | |  __/
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|
############################################
This is a data collector for super auto pets

It is meant to be used while watching a video

inputs:
    - round       => (round)
    - lives       => (lives)
    - Friends     => (name dmg hp effect)
    - Shop Friend => (name dmg hp)
    - Shop Food   => (name)

"""


done = False
while not done:
    isEnd = input("end?")
    if isEnd != "":
        with open("./data_collecter/data/data.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["end"])

    round = input("round: ")
    lives = input("lives: ")
    f1 = input("friend 1: ")
    f2 = input("friend 2: ")
    f3 = input("friend 3: ")
    f4 = input("friden 4: ")
    f5 = input("friend 5: ")
    s1 = input("shop 1: ")
    s2 = input("shop 2: ")
    s3 = input("shop 3: ")
    s4 = input("shop 4: ")
    s5 = input("shop 5: ")
    sf1 = input("shop food 1: ")
    sf2 = input("shop food 2: ")
    move = input("move: ")
    with open("./data_collecter/data/data.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [round, lives, f1, f2, f3, f4, f5, s1, s2, s3, s4, s5, sf1, sf2]
        )

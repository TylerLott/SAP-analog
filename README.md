# Python Super Auto Pets Analog

I started this project because I wanted to create a SAP analog that I could use to train bots that are able to roll the shit out of children who play this game.


## Game Overview

Player is in charge of building a team that will beat other teams 10 times. The teams are randomly selected from other players at the same round. 

Team information:
- friends
- lives
- round
- money
- won last round

Friends information:
- animal type
- exp
- hp
- dmg
- tmp_hp
- tmp_dmg
- effect
- ability
- ability level

Shop information:
- friends
- foods
- maxTier

Food information:
- food type
- exp
- hp
- dmg
- tmp_hp
- tmp_dmg
- effect

Possible move types:
- buy friend
- sell friend
- buy food for friend
- move friend
- freeze shop item
- roll
- end turn

Unknowns:
- specifics of team that will be fought
- certain animals have random abilities (i.e. give random friend hp)
- specifics of the fight (who attacks who, where random abilities are applied)
- probability of winning against any given team

## Minigames

Round 1 fighting
- given 10 money
- no start team
- play up until first battle

## Proposed architecture

- no clue at this point..

## Unit Tests

One Set of Tests
`python -m unittest tests/{nameOfTestSet}.py`

All Tests
`python -m unittest discover -s ./tests -p '*_test.py'`

## Pdoc3

`python -m pdoc --html ./src --force`

# Team

The team is the main unit that a player or AI will work with

### Varaibles

Round

- Number of the round the team is playing on

Shop

- Shop specific to a given team

Life

- Number of lives left

Money

- amount of money available in the shop

Friends

- array of the animals on a team

### Functions

moveFriend

sellFriend

buyFriend

buyFood

nextTurn

setState

getState

_str_

### State

State is the array representation of the team. It describes the possible interactions for the player or AI. This seem jank but will be fundamental in creating reinforcement learning agents to interact. It produced several different arrays.

This can be read in the following way:

- all arrays are one hot encoded, meaning they are either 1 or 0. 1 if present or possible, 0 if not.

**current**

[5 x number of animals + effects] for current team state

[7 x number of animals + effects] for current shop state

These will be kept as is and fed into the NN directly [12 x number of animals + effects (68)] thats like many, many different team states... which makes a NN reinforcement learning agent great for this because there will be new states almost every play through.

[5 x 4] for the stats, exp levels, and positions of the animals

- These are normalized to the greatest possible stat
- 50 for hp and dmg
- 6 for exp level

**combinatorics analysis of team state**

r can be 1-5, because a team can have 1-5 animals (this is assuming no empty)

n = 58, one for each animal

(n! / ((n-r)! \* r!) for r={1-5} and n=58) \* 10

r = 5

4582116

r = 4

424270

r = 3

30856

r = 2

1653

r = 1

58

total

5038953

\* 10

50,389,530 different possible team states (excluding hp, dmg, and exp stats and assuming all effects can be applied in shop (which I don't think is true))

lol thats a lot but chess has like ~10^29,241 possible games so I think this is doable, although I am not google deepmind... I also might need to combine the two arrays because I'm worried the animal position won't transfer. I may also need to only allow one move between fights, at least for the first little bit.

**possible moves**

[5 x 7] for shop options

- since you can buy food/animals from a max 7 different slots and place them on any of the 5 team slots

[1 x 15] for animal move options

- since you can swap the place of any of the animals

[1 x 20] for animal combine options

- since you can combine purchased animals into any of the other 4 slots that the animal is not in

[5 x 1] for animal sell

- since you can sell any animal in the team

[1 x 2] for roll and end turn

These are all flattened into one [1 x all (77)] array so the output from the NN can be a 1D array. This will probably be a filter on the NN instead of an actual input. (i.e. only making the availiable moves available)

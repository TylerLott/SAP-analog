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

These will be kept as is and fed into the NN directly

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

These are all flattened into one [1 x all] array so the output from the NN can be a 1D array. This will probably be a filter on the NN instead of an actual input. (i.e. only making the availiable moves available)

#random choice and random shuffle + index

import random

pets = ['dog', 'cat', 'moose']

print(pets)
print('random.choice() == ' + random.choice(pets))

petsShuffled = pets.copy()
random.shuffle(petsShuffled)
print('random.shuffle():', petsShuffled)

print('Dog index in pets: ', pets.index('dog'))
print('Dog index in petsShuffled: ', petsShuffled.index('dog'))

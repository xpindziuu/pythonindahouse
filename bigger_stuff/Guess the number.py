#Guess the number

import random, sys

print('Guess the number from 0 to 20. ')
print('You have only 5 tries.')
lifes = 5

randomNumber = random.randint(0,21)
print('DEBUG: ' + str(randomNumber))

while True:    
    while lifes > 0:
        guess = input()

        if int(guess) == randomNumber:
            print('Congrats, youve guessed correctly.')
            sys.exit()
        else:
            print('Nah its not that. Try again...')
            print('You still have ' + str(lifes - 1) + ' tries.')
            lifes -= 1
    
    print('You have run out of tries. Game Over.')
    sys.exit()

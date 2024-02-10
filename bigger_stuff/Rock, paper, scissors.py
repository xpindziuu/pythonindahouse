#Rock, paper, scissors

import random, sys

wins = 0
losses = 0
ties = 0

while True: 
    print('Your stats: ')
    print('Wins: ' + str(wins) + ' Losses: ' + str(losses) + ' Ties: ' + str(ties))

    print('Enter your move: (r)ock, (p)aper, (s)cissors.')
    print('Type exit to quit.')
    move = input()

    enemy = random.randint(0,2)
    
    if move == 'r' and enemy == 2:
        print('Congrats, you win!')
        wins += 1
    elif move == 'p' and enemy == 0:
        print('Congrats, you win!')
        wins += 1
    elif move == 's' and enemy == 1:
        print('Congrats, you win!')
        wins += 1
    elif move == 'r' and enemy == 0:
        print('AND THATS A TIE!')
        ties += 1
    elif move == 'p' and enemy == 1:
        print('AND THATS A TIE!')
        ties += 1
    elif move == 's' and enemy == 2:
        print('AND THATS A TIE!')
        ties += 1
    elif move == 's' and enemy == 0:
        print('Oh no, you lose. :(')
        losses += 1
    elif move == 'r' and enemy == 1:
        print('Oh no, you lose. :(')
        losses += 1
    elif move == 'p' and enemy == 2:
        print('Oh no, you lose. :(')
        losses += 1
    elif move == 'exit':
        sys.exit()

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
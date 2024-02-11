#magic 8ball

import random, sys

def magicball(answer):
    if answer == 1:
        return 'Its certain.'
    elif answer == 2:
        return 'Its decidedly so.'
    elif answer == 3:
        return 'Yes.'
    elif answer == 4:
        return 'Reply hazy try again.'
    elif answer == 5:
        return 'Ask again later.'
    elif answer == 6:
        return 'Concentrate and ask again.'
    elif answer == 7:
        return 'My reply is no.'
    elif answer == 8:
        return 'Outlook not so good.'
    elif answer == 9:
        return 'Very doubtful.'

while True:  
    magicRandom = random.randint(0,9)
    fortune = magicball(magicRandom)

    print(fortune)
    print('Enter f for next fortune.')
    decision = input()

    if decision != 'f':
        sys.exit()

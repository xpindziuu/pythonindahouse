#array magic 8ball

import random, sys

messages = [
    'Its certain.',
    'Its decidedly so.',
    'Yes.',
    'Reply hazy try again.',
    'Ask again later.',
    'Concentrate and ask again',
    'My reply is no.',
    'Outlook not so good.',
    'Very doubtful'
]

while True:
    print(messages[random.randint(0, len(messages)) - 1])

    a = input()
    if a == 'exit':
        sys.exit()
    elif a == '':
        continue

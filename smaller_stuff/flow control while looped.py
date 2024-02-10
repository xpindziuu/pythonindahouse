#flow control while looped

while True:

    burgier = 0

    while burgier <= 5:
        print('Hello, burgier :)')
        burgier += 1

    name = ''

    while name != 'your name.':
        print('Please type your name. ')
        name = input()

    print('Thank you.')


'''
> Program types out message about burgier 6 times.
> Then asks user to type your name.
    > if user types your name. then program thanks him.
    > if not program asks again.

+ program loops on end (ctrl + c to exit)
    *adding break on end will basically make this loop useless 
'''
#working with lists

catNames = []

while True:
        print('Enter name of the ' + str(len(catNames) + 1) + ' cat.')
        print('Type nothing to stop.')
        name = input()

        if name == '':
                break
        
        catNames += [name]

print('The cat names are: ')

for name in catNames:
        print('     ' + name)
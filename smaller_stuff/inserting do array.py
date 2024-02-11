#inserting to array and removing stuff

pets = ['dog', 'cat', 'moose']
print('Before: ', pets)


pets.insert(2, 'bat')
print('After insert: ', pets)

pets.append('hamster')
print('After append: ', pets)

pets.remove('bat')
print('After bats extermination: ', pets)
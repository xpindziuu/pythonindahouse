#conways game of life

import random, time, copy, os

WIDTH = 60
HEIGHT = 20

nextCells = []

for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # Living cell
        else:
            column.append(' ') # Dead cell

    nextCells.append(column)

while True:
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')
        
        print()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCord = (x - 1) % WIDTH
            rightCord = (x + 1) % WIDTH
            upCord = (y - 1) % HEIGHT
            downCord = (y + 1) % HEIGHT

            numNeighbors = 0

            if currentCells[leftCord][upCord] == '#':
                numNeighbors += 1
            if currentCells[x][upCord] == '#':
                numNeighbors += 1
            if currentCells[rightCord][upCord] == '#':
                numNeighbors += 1
            if currentCells[leftCord][y] == '#':
                numNeighbors += 1
            if currentCells[rightCord][y] == '#':
                numNeighbors += 1
            if currentCells[leftCord][downCord] == '#':
                numNeighbors += 1
            if currentCells[x][downCord] == '#':
                numNeighbors += 1
            if currentCells[rightCord][downCord] == '#':
                numNeighbors += 1
            
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = ' '
    
    time.sleep(0.5)
    os.system('cls')
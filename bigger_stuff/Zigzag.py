#Zigzag

import time, sys

space = 0
spaceIncreasing = 1 # 1 - for increasing; 0 - for decreasing

try:
    while True:
        print(' ' * space, end='')
        print('*********')
        
        time.sleep(0.1)
        
        if spaceIncreasing:
            space += 1

            if space == 20:
                spaceIncreasing = 0;
        else:
            space -= 1

            if space == 0:
                spaceIncreasing = 1;

except KeyboardInterrupt:
    sys.exit()
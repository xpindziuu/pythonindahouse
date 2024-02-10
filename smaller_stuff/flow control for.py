#flow control for

print('My name is ')

for i in range(5):
    print('Zbys five times [' + str(i + 1) +'] ')

total = 0

#from 0 to 100, adding 1 on every loop
for num in range(101):
    print(total)
    total =+ num
print('----> ' + str(total))
#Handling errors
def spam(devideBy):
    try:
        return 42 / devideBy
    except ZeroDivisionError:
        print('Error, but not crashing entire app.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))


def spam2(devideBy):
    return 42 / devideBy
    
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))

except ZeroDivisionError:
    print('Another error, but app is still running.')
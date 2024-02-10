#My first program
print('Hello world!')

#input() pozwala wpisać zmienna
print('What is your name?')
myName = input()

print('Nice to meet you! ' + myName)

#len(myName) zwraca ile znaków ma string myName
print('Lenght of your name is: ' + str(len(myName)))

print('What is your age?')
myAge = input()

#str(int(myAge) + 1) <- str() operacja jako string (aby możliwe było wyświetlenie jej miedzy stringami)
#                    <- int() operacja jako int (aby dodać do wieku jeden)
#                    <- int(myAge) + 1      dodaje do wieku jeden
print('You will be ' + str(int(myAge) + 1) + ' in a year!')

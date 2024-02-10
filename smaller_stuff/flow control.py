#flow control

print('Type your name: ')
name = input()

zbysPassword = 'marchewka'

if name == 'Zbys' or name == 'zbys':
    print('Welcome, Zbys')

    print('Enter your password:')
    passTry = input()
    
    if passTry == zbysPassword:
        print('Correct password')
    else:
        print('Incorrent password')
else:
    print('This isnt Zbys, go away pls :(')


#User prompted to enter name
#       if name ist zbys or Zbys then program ask user to go away
#       if name is zbys or Zbys then program processed to prompt user to enter predefined password
#              if user enter wrong password then program displays according message
#              if user enter correct password then program displays according messege
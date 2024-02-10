#flow control continue

while True:
    print('Who you are?: ')
    name = input()

    if name != 'Zbys' and name != 'zbys':
        continue

    print('Hello, Zbys. Whats the password?: ')
    password = input()

    if password == 'marchewka':
        break

print("Access granted.")


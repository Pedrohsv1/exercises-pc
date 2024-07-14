values_rectangle = input('').split()
values_game = input('')

positionX = int(values_game.split()[0])
positionY = int(values_game.split()[1])
positionXBoolean = False
positionYBoolean = False

values_rectangle0 = int(values_rectangle[0])
values_rectangle1 = int(values_rectangle[1])
values_rectangle2 = int(values_rectangle[2])
values_rectangle3 = int(values_rectangle[3])

if positionX >= values_rectangle0 and positionX <= values_rectangle2:
    positionXBoolean = True
if positionY >= values_rectangle1 and positionY <= values_rectangle3:
    positionYBoolean = True

if positionXBoolean and positionYBoolean:
    print('Dentro!')
else:
    print('Fora!')
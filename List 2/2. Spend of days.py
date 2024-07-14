number = float(input(''))
higher = number
while number != 0:
    if number > higher:
        higher = number
    number = float(input(''))
if higher == 0:
    print('Você não teve gastos hoje!')
else:
    print('O seu maior gasto hoje foi R${: .2f}'.format(higher))
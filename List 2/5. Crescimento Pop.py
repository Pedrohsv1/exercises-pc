n = int(input())

for x in range(n):
    values = input().split(' ')
    popA  = int(values[0])
    popB  = int(values[1])
    percA = float(values[2])
    percB = float(values[3])

    age = 0

    while age < 101:
        popA = int( popA * (1 + percA/100))
        popB = int( popB * (1 + percB/100))

        age += 1

        if(popA > popB):
            break
    if(age > 100):
        print('Mais de 1 seculo.')
    else:
        print('{} anos.'.format(age))



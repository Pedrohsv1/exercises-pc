number = int(input())
if number <= 0:
    print('O número deve ser maior que 0.')
else:
    factorial = 1
    for n in range(number):
        factorial = factorial * (n+1)
    print('Resultado do fatorial: {}'.format(factorial))


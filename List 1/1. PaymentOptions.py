import math

value = int(input(''))
typeofpayment = input('')

while typeofpayment != 'V' and  typeofpayment != 'P':
    
    print('Tente novamente! você precisa colocar V ou P.')

    typeofpayment = input('')

if typeofpayment == 'V':

    valueFivePercent = value*0.95

    print('Valor à pagar: {}'.format(math.trunc(valueFivePercent)))

elif typeofpayment == 'P':

    valueEightPercent = value*1.08
    valueDivided = valueEightPercent/3

    print('Valor à pagar: {}'.format(math.trunc(valueEightPercent)))
    print('''Parcela 1: {0}
Parcela 2: {0}
Parcela 3: {0}'''.format(math.trunc(valueDivided)))
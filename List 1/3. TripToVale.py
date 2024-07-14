value = input('')
list_values = value.split(' ')

kelvin, celsius, fahrenheit = 0, 0, 0

valueNumber = float(list_values[0])
valueType = list_values[1]

if valueType == 'K':
    kelvin = valueNumber
    celsius = kelvin - 273.15
    fahrenheit = celsius * 1.8 + 32.0
elif valueType == 'C':
    celsius = valueNumber
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.8 + 32.0
elif valueType == 'F':
    fahrenheit = valueNumber
    celsius = ( fahrenheit - 32.0 ) / 1.8
    kelvin = celsius + 273.15
else: 
    print('Ocorreu algum erro!')

print('''Temperatura em Celsius:{0: .2f} °C
Temperatura em Fahrenheit:{1: .2f} °F
Temperatura em Kelvin:{2: .2f} K'''.format(celsius, fahrenheit, kelvin))



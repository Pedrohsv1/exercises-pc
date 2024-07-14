userInputs = input().split(',')
numbers = []
if(len(userInputs) > 1):
    for n in userInputs:
        if(numbers.count(float(n)) == 0):
            numbers.append(float(n))
    numbers.sort(reverse=True)


    if(len(numbers) > 1):
        print(numbers[1])
    else:
        print('Não é possível determinar o segundo maior valor com menos de dois valores distintos.')
else:
    print('Não é possível determinar o segundo maior valor com menos de dois elementos.')
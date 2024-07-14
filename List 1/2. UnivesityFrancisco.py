N1 = float(input(''))
N2 = float(input(''))
N3 = float(input(''))

average = ((N1*2) + (N2*3) + (N3*4)) / 9

if average >= 7:
    print('Francisco está aprovado')
elif average >= 3 and average < 7:
    print('Francisco está em prova final')
else:
    print('Francisco está reprovado')

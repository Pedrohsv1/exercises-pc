n = int(input())
for x in range(n):
    aux    = ""
    
    for j in range(n):
        if(j > x):
            aux = aux + '{}'.format(j-x + 1)
        elif(j == x):
            aux = aux + '{}'.format(1)
        else:
            aux = aux + '{}'.format(x-j + 1)

        if(j < n-1):
            aux = aux + ' '
    print(aux)
        
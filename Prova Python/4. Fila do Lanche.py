times = int(input())

for _ in range(times):
    qtd_values = int(input())
    values = input().split(' ')

    copy_values = values.copy()
    copy_values.sort(reverse=True)

    count = 0

    print(values, copy_values)

    if(qtd_values >= 2):
        if(int(copy_values[0]) < int(copy_values[0])):
            count = qtd_values
        else:
            for x in range(qtd_values):
                if(values[x] == copy_values[x]):
                    count += 1
    else:
        count = 1
    
    print(count)
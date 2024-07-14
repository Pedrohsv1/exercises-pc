def SumOfOdds(X, Y):
    isXOdd = X%2
    sum = 0
    if isXOdd == 0:
        firstOddNumber = X + 1
        for _ in range(Y):
            sum = sum + firstOddNumber + _ * 2
    else:
        firstOddNumber = X
        for _ in range(Y):
            sum = sum + firstOddNumber + _ * 2
    
    return(sum)

testTimes = int(input())
sum = []
for _ in range(testTimes):
    XandY = input().split()
    sum.append(SumOfOdds( int(XandY[0]), int(XandY[1])))

for _ in sum:
    print(_)


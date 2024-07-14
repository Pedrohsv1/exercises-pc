userInput = input()
changedValue = input()
newValue = input()

newList = userInput[1:len(userInput)-1].split(',')

emptyList = []

count = 0

for item in newList:

    if(item.strip() == changedValue):
        count += 1
        emptyList.append(newValue)
    else:
        emptyList.append(item.strip())
    
if(count == 0):
    print('Item não presente no inventário.')
else:
    print(emptyList)
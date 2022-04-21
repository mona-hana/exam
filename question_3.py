# question 3



count = int(input("please enter number of list : "))
#if not count.isdigit() : 
i = 0
numList = []
while i < count:
    num = int(input("your number :"))
    numList.insert(i, num)
    i += 1

for number in range(len(numList)):
    min = number

    for j in range(number+1, (len(numList))):
        if numList[min] > numList[j]:
            min = j

    
    numList[min], numList[number] = numList[number], numList[min]

print(numList)
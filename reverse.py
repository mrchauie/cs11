numList = [1 ,3 ,6, 93, 4, 3, 5, 8]

#swap method
#save the length of list for readibility
length = len(numList)
middle = length // 2 #double slash is integer division
for i in range(middle):
    #swap
    temp = numList[i]
    numList[i] = numList[length-i-1]
    numList[length-i-1] = temp

print(numList)

#swap using a temp list
#initialize the temp list
tempList = []
startIndex = 0 #use variable for readibility
for i in range(length-1, startIndex-1, -1): #step down
    tempList.append(numList[i])

numList = tempList
print(numList)




list1 = ['joe', 'bob', 'anne']
list2 = ['smith', 'lee', 'frank']
list3 = []
for i in range(len(list1)):
    list3.append([list1[i], list2[i]])

#how do you manipulate list3 to capitalize the 
# first letter of first and last name
# .capitalize(), .upper(), .title()

#Please sort the customer database by last name
#use .sort() with a key parameter



#sorting list of tuples by second tuple element
def secondElement(element):
    return element[1]

#['anne', 'frank', 'mary']
def middleName(element):
    return element[2]

list3.sort(key=secondElement)
# #or
list3.sort(key=lambda a: a[1])

print(list3)
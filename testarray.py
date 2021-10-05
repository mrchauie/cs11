cards = [3,2,9,5,6,10]
length = len(cards) #this should return 6
# temp = []

# for i in range(length):
#     cards_index = length-i-1
#     temp.insert(i, cards[cards_index])

# print(cards)
# print(temp)

for i in range(length//2):
    temp = cards[i]
    cards[i]= cards[length-i-1]
    cards[length-i-1] = temp

print(cards)
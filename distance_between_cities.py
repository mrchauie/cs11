distance_between_cities = [3, 10, 12, 5, 3, 10]

distance = []
sum_left = 0
sum_right = 0
for i in range(len(distance_between_cities)+1):
    #sum the left and put it in a list
    for j in range(i-1, -1, -1):
        sum_left = sum_left + distance_between_cities[j]
        distance.insert(0, sum_left)

    #add the 0
    distance.append(0)

    #sum the right and put it in a list
    for k in range(i, len(distance_between_cities)):
        sum_right = sum_right + distance_between_cities[k]
        distance.append(sum_right)
    
    print(distance)
    sum_left = 0
    sum_right = 0
    distance = []


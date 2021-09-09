def BinarySearch (array, n) :

    beg = 0
    end = len(array) - 1 

    while (beg <= end) :

        mid = int(beg + (end-beg)/2)

        if (array[mid] == n) :
            return mid 
        elif (array[mid] < n) :
            beg = mid + 1;  
        else :
            end = mid - 1

    return -1; 

array = [ 3, 5, 7, 11, 12, 16, 17, 52, 64, 101 ]

n = int(input("Element to search : "))
index = BinarySearch (array, n)

if (index != -1) :
    print("Element found at index : " + str(index))
else :
    print("Element not found. ")
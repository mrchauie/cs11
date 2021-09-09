
# Function to merge the sorted sub-arrays into a bigger array.
def Merge (aux_array, array, low, mid, high):

    left_index = low
    right_index = mid + 1
    aux_index = low

    # Merge elements from array[low : mid] and array[mid+1 : high]
    #                           ^                     ^
    #                           |                     |
    #                         left_index         right_index

    # Pick the smaller number between the left part and the right part
    while (left_index <= mid and right_index <= high):
        if (array[left_index] <= array[right_index]):
            aux_array[aux_index] = array[left_index]
            aux_index += 1
            left_index += 1
        else:
            aux_array[aux_index] = array[right_index]
            aux_index += 1
            right_index += 1

    if (left_index <= mid):
        # There are still some unpicked numbers in the left part
        for i in range(left_index, mid + 1):
            aux_array[aux_index] = array[i]
            aux_index += 1
    else:
        # There are still some unpicked numbers in the right part
        for i in range(right_index, high + 1):
            aux_array[aux_index] = array[i]
            aux_index += 1

    # Copy numbers from the sorted auxiliary array into the original array
    for i in range(low, high + 1):
        array[i] = aux_array[i]

# MergeSort function splits each sub-array till only a single element is available in the sub-array 
# and then proceeds with the merge of the sub-arrays into a bigger auxiliary array.
def MergeSort (aux_array, array, low, high):

    if (low < high):

       mid = int((low + high)/2)

       MergeSort (aux_array, array, low, mid)    # Recursively splits left half of the array
       MergeSort (aux_array, array, mid+1, high) # Recursively splits right half of the array

       Merge (aux_array, array, low, mid, high)  # Merge left and right half of the array keeping it sorted.

def main():

    array = [7, 3, 5, 2, 4, 1, 8, 6, 0, 10, 9]
    print("Unsorted array: " + str(array))

    # Allocate space for the auxiliary vector
    aux_array = [None] * len(array)

    MergeSort (aux_array, array, 0, len(array)-1)

    print("Sorted array using merge sort: " + str(array))

if __name__ == "__main__" :
    main()

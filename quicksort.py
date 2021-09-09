#!/usr/bin/python3

def Partition(array, start, end):

    j = start

    # Keep placing elements less than the pivot (array[end]) element to the left
    for i in range(start, end):
        if (array[i] < array[end]):
            # Swap array[i] with array[j]
            array[i], array[j] = array[j], array[i]
            j += 1
    
    # Place the pivot (array[end]) at its final position and return the pivot index
    # for partitioning the array
    # Swap array[j] with array[end]
    array[j], array[end] = array[end], array[j]
    return j

def QuickSort(array, start, end):

    p = None; # Tracks partition

    if (start < end):
        p = Partition (array, start, end)
        QuickSort (array, start, p-1)
        QuickSort (array, p+1, end)

def main():

    array = [7, 3, 5, 2, 4, 1, 8, 6]
    print("Unsorted array: " + str(array))

    QuickSort(array, 0, len(array)-1);

    print("Sorted array using Quicksort: " + str(array))

if __name__ == "__main__":
    main()


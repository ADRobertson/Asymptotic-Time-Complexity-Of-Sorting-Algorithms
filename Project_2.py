import random, time


#bubble sort algorithm
def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
    return arr


#merge sort algorithm
def merge_sort(arr):
    # The last array split
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # Merge each side together
    return merge(left, right, arr.copy())


def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):

        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


#quick sort algorithm

# Function to find the partition position
def partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1

# function to perform quicksort


def quickSort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)
    return array


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

 # See if left child of root exists and is greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

 # See if right child of root exists and is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

 #  swap if needed
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])

  # Heapify the root.
        heapify(arr, n, largest)


# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)


 # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0)
    return arr

#helper function so I don't have to type the time thing over and over
def timer():
    t = time.perf_counter()
    return t

# Driver code to test above

def main():
    numElem = 10000

    #need 4 copies of a randomly generated array

    #loop to generate n element array of random integers
    arr = []
    for x in range(numElem):
        int = random.randint(0, 200)
        arr.append(int)
    arrBubble = arr
    arrMerge = arr
    arrQuick = arr
    arrHeap = arr
    #print(arrBubble)
    #-----------------------------------------------------------------------------
    #array to be sent to bubbleSort
    tbs0 = timer()
    arrBubble = bubble_sort(arr)
    tbs = timer()
    #print("\nBubble Sorted Array:", arrBubble)
    bubbleTime = tbs - tbs0
    print("Sorting time for Bubble Sort:", bubbleTime, "seconds")
    #print(arrMerge)
    #-----------------------------------------------------------------------------
    tm0 = timer()
    arrMerge = merge_sort(arrMerge)
    tm = timer()
    mergeTime = tm - tm0
    #print("\nMerge Sorted Array:", arrMerge)
    print("Sorting time for Merge Sort:", mergeTime, "seconds")
    #-----------------------------------------------------------------------------
    tq0 = timer()
    arrQuick = quickSort(arrQuick, 0, len(arrQuick) - 1)
    tq = timer()
    quickTime = tq - tq0
    #print("\nQuick Sorted Array:", arrQuick)
    print("Sorting time for Quick Sort:", quickTime, "seconds")
    #-----------------------------------------------------------------------------
    th0 = timer()
    arrHeap = heapSort(arrHeap)
    th = timer()
    heapTime = th - th0
    print("\nHeap Sorted Array:", arrHeap)
    print("Sorting time for Heap Sort:", heapTime, "seconds.")




#this calls main for runtime
main()

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

#helper function to copy array without clogging up main...
def copyArray(arr):
    returnArray = []
    for x in arr:
        returnArray.append(x)
    return returnArray

def SortTimer(arr, sortRequested):
    if (sortRequested == "Bubble"):
        t0 = timer()
        arr = bubble_sort(arr)
        t = timer()
        time = t-t0
    if (sortRequested == "Merge"):
        t0 = timer()
        arr = merge_sort(arr)
        t = timer()
        time = t-t0
    if (sortRequested == "Quick"):
        t0 = timer()
        arr = quickSort(arr, 0, len(arr) - 1)
        t = timer()
        time = t-t0
    if (sortRequested == "Heap"):
        t0 = timer()
        arr = heapSort(arr)
        t = timer()
        time = t-t0
    return time

# Driver code to test above

def main(numElements):

    #need 4 copies of a randomly generated array

    #loop to generate n element array of random integers
    arr = []
    for x in range(numElements):
        int = random.randint(0, 200)
        arr.append(int)

    #lists for storing runtimes for average, best, worst cases
        #index 0 = average, 1 = best, 2 = worst
    bubbleTimes = []
    mergeTimes = []
    quickTimes = []
    heapTimes = []


    #need function to automatically copy array wihout being pointers
        #these are average cases for all, scrambled arrays
    arrBubble = copyArray(arr)
    arrMerge = copyArray(arr)
    arrQuick = copyArray(arr)
    arrHeap = copyArray(arr)

        #these will be best cases
    arrBubbleBest = copyArray(arr)
    arrMergeBest = copyArray(arr)
    arrQuickBest = copyArray(arr)
        #these will be worst cases
    arrBubbleWorst = copyArray(arr)
    arrMergeWorst = copyArray(arr)
    arrQuickWorst = copyArray(arr)
        #best case for BUBBLE SORT is when the array is already sorted
    arrBubbleBest = bubble_sort(arrBubbleBest)
        #worst case for BUBBLE SORT i when the array is reverse SORTED
    arrBubbleWorst = sorted(arrBubbleWorst, reverse=True)

        #best, average, worst case for MERGE SORT are all the same
        #asymptotic time complexity, so it can be skipped in that regard

        #best case for QUICK SORT is when the array is already sorted
    arrQuickBest = merge_sort(arrQuickBest)
        #worst case for QUICK SORT is
    arrQuickWorst = sorted(arrQuickWorst, reverse=True)

        #best case for HEAP SORT is when all the elments are equal, so it gets
        #a special array
    arrHeapBest = []
    num = random.randint(0, 200)
    for x in range(numElements):
        arrHeapBest.append(num)
        #worst case for HEAP SORT is when all elements of an array are distinct!
    arrHeapWorst = []
    for x in range(numElements):
        arrHeapWorst.append(x)
    #-----------------------------------------------------------------------------
    bubbleTimes.append(SortTimer(arrBubble, "Bubble"))
    bubbleTimes.append(SortTimer(arrBubbleBest, "Bubble"))
    bubbleTimes.append(SortTimer(arrBubbleWorst, "Bubble"))
    #-----------------------------------------------------------------------------
    mergeTimes.append(SortTimer(arrMerge, "Merge"))
    #-----------------------------------------------------------------------------
    #quickTimes.append(SortTimer(arrQuick, "Quick"))
    #quickTimes.append(SortTimer(arrQuickBest, "Quick"))
    #quickTimes.append(SortTimer(arrQuickWorst, "Quick"))
    #-----------------------------------------------------------------------------
    heapTimes.append(SortTimer(arrHeap, "Heap"))
    heapTimes.append(SortTimer(arrHeapBest, "Heap"))
    heapTimes.append(SortTimer(arrHeapWorst, "Heap"))
    #-----------------------------------------------------------------------------
    file = open("output" + str(numElements) + ".txt", 'w')

    file.write("Average Case BubbleSort time for " + str(numElements) + " elements: " + str(bubbleTimes[0]) + " seconds.")
    file.write("\nBest Case BubbleSort time for " + str(numElements) + " elements: " + str(bubbleTimes[1]) + " seconds.")
    file.write("\nWorst Case BubbleSort time for " + str(numElements) + " elements: " + str(bubbleTimes[2]) + " seconds.")

    file.write("\n\nAverage, Best, and Worst Case MergeSort Time for " + str(numElements) + " elements: " + str(mergeTimes[0]) + " seconds.")

    #file.write("\n\nAverage Case QuickSort time for " + str(numElements) + " elements: " + str(quickTimes[0]) + " seconds.")
    #file.write("\n\nBest Case QuickSort time for " + str(numElements) + " elements: " + str(quickTimes[1]) + " seconds.")
    #file.write("\n\nWorst Case QuickSort time for " + str(numElements) + " elements: " + str(quickTimes[2]) + " seconds.")

    file.write("\n\nAverage Case HeapSort time for " + str(numElements) + " elements: " + str(heapTimes[0]) + " seconds.")
    file.write("\nBest Case HeapSort time for " + str(numElements) + " elements: " + str(heapTimes[1]) + " seconds.")
    file.write("\nWorst Case HeapSort time for " + str(numElements) + " elements: " + str(heapTimes[2]) + " seconds.")
    file.close()
    #-----------------------------------------------------------------------------


#this calls main for runtime
#main(10)
main(1000)
#main(10000)

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
def partition(array, begin, end):
    pivot_idx = begin
    for i in xrange(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]

    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx

def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    
    quick_sort_recursion(array, begin, pivot_idx-1)
    
    quick_sort_recursion(array, pivot_idx+1, end)

def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    
    return quick_sort_recursion(array, begin, end)



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
 
 
# Driver code to test above
 
arr = [12, 11, 13, 5, 6, 7, ]
heapSort(arr)
n = len(arr)
print('Sorted array is')
for i in range(n):
    print(arr[i])



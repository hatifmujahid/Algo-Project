
def insertion_sort(arr, low, n):
    for i in range(low + 1, n + 1):
        val = arr[i]
        j = i
        while j>low and arr[j-1]>val:
            arr[j]= arr[j-1]
            j-= 1
        arr[j]= val
 

def partition(arr, low, high):
    pivot = arr[high]
    i = j = low
    for i in range(low, high):
        if arr[i]<pivot:
            arr[i], arr[j]= arr[j], arr[i]
            j+= 1
    arr[j], arr[high]= arr[high], arr[j]
    return j
 
def quick_sort(arr, low, high):
    if low<high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot + 1, high)
        return arr
 
def hybrid_quick_sort(arr, low, high):
    while low<high:        
        if high-low + 1<10:
            insertion_sort(arr, low, high)
            break
        else:
            pivot = partition(arr, low, high)
            if pivot-low<high-pivot:
                hybrid_quick_sort(arr, low, pivot-1)
                low = pivot + 1
            else:
                hybrid_quick_sort(arr, pivot + 1, high)
                high = pivot-1

def book_725(arr):
    hybrid_quick_sort(arr, 0, len(arr)-1)
    
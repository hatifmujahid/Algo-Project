from random import randint
import time
import matplotlib.pyplot as plt 
import numpy as np
global op
op = 5000
def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        j = i
        while j > low and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
        
def partition(a, low, high): #lomuto partition scheme
    i = low - 1 #directly to the left of our specified low-high range
    pivot = a[high] #pivot is the last value in our range, the index equal to high parameter
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[high] = a[high], a[i+1]
    return i+1

def quicksort_inplace(a, low=0, high=None):
    
    if high is None:
        high = len(a) - 1

    if low < high:
        if high - low + 1 < op:
            # Size of the subarray is less than the threshold, insertion sort
            insertion_sort(a, low, high)
            return
        # Size of the subarray is greater than the threshold, quicksort
        pivot_index = partition(a, low, high)
        quicksort_inplace(a, low, pivot_index - 1)
        quicksort_inplace(a, pivot_index + 1, high)
def book_725(arr):
    # print("threshold is 50000")
    # start = time.time()
    # op = 50000
    # quicksort_inplace(arr)
    # end = time.time()
    # result2 = end-start

    # print("threshold is 75000")
    # start = time.time()
    # op = 75000
    # quicksort_inplace(arr)
    # end = time.time()
    # result3 = end-start
    print(len(arr), max(arr)-min(arr))
    print("Enter the threshold: ")
    op = int(input())
    prompt = "threshold is"
    print(prompt, op)
    start = time.time()
    quicksort_inplace(arr)
    end = time.time()
    result4 = end-start

    data = {'threshold is ':result4}
    threshold = list(data.keys())
    values = list(data.values())

    fig,ax = plt.subplots()
    ax.set_ylabel('Time in seconds')
    ax.set_xlabel('Threshold')
    ax.set_title('Graph of time against threshold')
    plt.bar(threshold, values, color = 'blue', width = 0.4)
    plt.show()

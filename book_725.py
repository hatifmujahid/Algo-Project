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
        
def partition(a, low, high): 
    i = low - 1 
    pivot = a[high] 
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
            
            insertion_sort(a, low, high)
            return
        # Size of the subarray is greater than the threshold, quicksort
        pivot_index = partition(a, low, high)
        quicksort_inplace(a, low, pivot_index - 1)
        quicksort_inplace(a, pivot_index + 1, high)
def book_725(arr):
    print(len(arr), max(arr)-min(arr))
    print("Enter the threshold: ")
    op = int(input())
    prompt = "threshold is"
    print(prompt, op)
    start = time.time()
    quicksort_inplace(arr)
    end = time.time()
    result4 = end-start
    return result4
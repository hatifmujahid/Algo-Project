from random import randint
import math
import matplotlib.pyplot as plt 
import numpy as np
import time
from book_725 import book_725
from book_824 import book_824
def count_sort(arr):
    start = time.time()
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]
  
    for i in range(0, len(arr)):
        count_arr[arr[i]-min_element] += 1
  
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
  
    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1
  
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]
    end = time.time()
    return (end- start)
def _bucket_bucket(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up: 
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up     
    return b     
              
def bucketSort(x):
    arr = []
    slot_num = 10 # 10 means 10 slots, each
    for i in range(slot_num):
        arr.append([])
          
    # Put array elements in different buckets 
    for j in x:
        index_b = int(slot_num * j) 
        arr[index_b].append(j)
      
    for i in range(slot_num):
        arr[i] = insertionSort_bucket(arr[i])
          
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x
def countingSort_radix(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


def radixSort(array):
    start = time.time()
    max_element = max(array)

    place = 1
    while max_element // place > 0:
        countingSort_radix(array, place)
        place *= 10
    end = time.time()
    return (end-start)

def quickSort(array):  # in-place | not-stable
    start = time.time()
    if len(array) <= 1:
        return array
    smaller, equal, larger = [], [], []
    pivot = array[randint(0, len(array) - 1)]
    for x in array:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)
    end = time.time()
    return end-start
def heapify(arr, N, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < N and arr[largest] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < N and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, N, largest)
 
# The main function to sort an array of given size
 
 
def heapSort(arr):
    start = time.time()
    N = len(arr)
 
    # Build a maxheap.
    for i in range(N//2 - 1, -1, -1):
        heapify(arr, N, i)
 
    # One by one extract elements
    for i in range(N-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
    end = time.time()
    return end-start

def bubbleSort(arr):
    start = time.time()
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    end = time.time()
    return end-start
def mergeSort(arr):
    start = time.time()
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    
    end = time.time()
    return end -start

def insertionSort(arr):
    start = time.time()
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    
    end = time.time()
    return end-start

 
def main_code(float_list, int_list):
      
    time1 = count_sort(int_list)
    time2 = radixSort(int_list)
    time3 = quickSort(int_list)
    time4 = heapSort(int_list)
    time6 = mergeSort(int_list)
    time7 = insertionSort(int_list)
    time5 = bubbleSort(int_list)
    time8 = book_725(int_list)
    time9 = book_824(int_list)


    if max(int_list)>1 or min(int_list)<0:
        data = {'Counting Sort':time1, 'Radix Sort':time2, 'quickSort': time3,'heapSort':time4,'Bubble sort': time5,'mergeSort':time6 , 'insertionSort':time7, 'Book 7.25':time8, 'Book 8.24':time9}
        print(data.values())
        sorting_algos = list(data.keys())
        values = list(data.values())

        fig,ax = plt.subplots()
        ax.set_ylabel('Time in seconds')
        ax.set_xlabel('Sorting algo names')
        ax.set_title('Graph of time')
        plt.bar(sorting_algos, values, color = '#f7b705', width = 0.4)
        plt.show()  

import random
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



def main_code(float_list, int_list):
    
    book_824(int_list, 5,22-1)
    book_725(int_list)
    time1 = count_sort(int_list)
    time2 = radixSort(int_list)
    if max(int_list)>1 or min(int_list)<0:
        data = {'Counting Sort':time1, 'Radix Sort':time2, 'Bucket Sort': 0}
        sorting_algos = list(data.keys())
        values = list(data.values())

        fig,ax = plt.subplots()
        ax.set_ylabel('Time in seconds')
        ax.set_xlabel('Sorting algo names')
        ax.set_title('Graph of time (Bucket sort is not possible with this array)')
        plt.bar(sorting_algos, values, color = 'black', width = 0.4)
        plt.show()  
    else:
        time3 = bucketSort(float_list)
        data = {'Counting Sort':time1, 'Radix Sort':time2, 'Bucket Sort':time3}
        sorting_algos = list(data.keys())
        values = list(data.values())

        fig,ax = plt.subplots()
        ax.set_ylabel('Time in seconds')
        ax.set_xlabel('Sorting algo names')
        ax.set_title('Graph of time')
        plt.bar(sorting_algos, values, color = 'blue', width = 0.4)
        plt.show()

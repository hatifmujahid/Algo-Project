import pygame
import random
import math
import matplotlib.pyplot as plt 
import numpy as np
import time
from noncomparision import *
from ui_file import *
pygame.init()
class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BACKGROUND_COLOR = BLACK
    BLUE = 0, 0, 255
    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    FONT = pygame.font.SysFont('Times New Roman', 30)
    LARGE_FONT = pygame.font.SysFont('Times New Roman', 40)

    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualization")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2


def draw(draw_info, algo_name, ascending):
    #window is filled with whwite color 
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.GREEN)
    draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2, 1))

    # font rendered
    controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, draw_info.BLUE)
    # display it on the screen
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2, 55))
    # sorting wala part display
    sorting = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort | S - Selection Sort | H - Heap Sort | Q - Quick Sort", 1, draw_info.BLUE)
    # display it on the screen
    draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2, 85))
    
    #list is drawn after all above
    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD,
                        draw_info.width-draw_info.SIDE_PAD, draw_info.height-draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate (lst):
        x = draw_info.start_x + i *draw_info.block_width
        y = draw_info.height - (val-draw_info.min_val)*draw_info.block_height

        color = draw_info.GRADIENTS[i % 3]

        if i in color_positions:
            # the index will map to a color
            color = color_positions[i]
        pygame.draw.rect(draw_info.window, color, (x,y,draw_info.block_width,draw_info.height))

    if clear_bg:
        pygame.display.update()
def generating_starting_list(n,min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst

def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            num1 = lst[j]
            num2 = lst[j+1]

            if (num1>num2 and ascending) or (num1<num2 and not ascending):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                draw_list(draw_info, {j:draw_info.GREEN, j+1: draw_info.RED},True)
                # a swap is done and a true value is sent called a generator
                #transfers control after every swap
                yield True 
    return lst

def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for step in range (len(lst)):
        min_idx = step

        for i in range(step+1, len(lst)):
            if (lst[i] < lst[min_idx] and ascending) or (lst[i] > lst[min_idx] and not ascending):
                min_idx = i
            
        lst[step], lst[min_idx] = lst[min_idx], lst[step]
        draw_list(draw_info, {step:draw_info.GREEN, min_idx:draw_info.RED}, True)
        yield True
    
    return lst

def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(1, len(lst)):
        current = lst[i]

        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current
            draw_list(draw_info, {i - 1: draw_info.GREEN, i: draw_info.RED}, True)
            yield True

    return lst
def partition(draw_info,array,low,high):
    i = ( low - 1 )
    x = array[high]
 
    for j in range(low , high):
        if   (array[j] <= x and ascending) or (array[j] > x and not ascending):
 
            i = i+1
            array[i],array[j] = array[j],array[i]
            draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.RED}, True)
            yield True
    array[i+1],array[high] = array[high],array[i+1]
    draw_list(draw_info, {i + 1: draw_info.GREEN, high: draw_info.RED}, True)
    yield True
    return (i+1)
 
def QuickSort(draw_info, ascending=True):
    array = draw_info.lst
    low = 0
    high = len(array)
    #  auxiliary stack
    size = high - low + 1
    stack = [0] * (size)
 
    top = -1
 
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high
 
    # Keep popping from stack while is not empty
    while top >= 0:
 
        # Pop high and low
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1
 
        # sorted array
        p = partition( draw_info,array, low, high )

        # push left side to stack
        if p-1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1

        #  push right side to stack
        if p+1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high

def heapify(draw_info, arr,n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        draw_list(draw_info,{i:draw_info.GREEN, largest:draw_info.RED}, True)
        heapify(draw_info,arr, n, largest)

  
def heapSort(draw_info, ascending=True):
    arr = draw_info.lst
    n = len(arr)

    # Build max heap
    for i in range(n//2, -1, -1):
        heapify(draw_info,arr, n, i)

    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]

        draw_list(draw_info,{i:draw_info.GREEN, 0:draw_info.RED}, True)
        yield True
        # Heapify root element
        heapify(draw_info,arr, i, 0)
# main function to do heap sort
def heapSort_descending(draw_info, ascending=True):
     
    # Build heap (rearrange array)
    for i in range(int(n / 2) - 1, -1, -1):
        heapify(draw_info,arr, n, i)
 
    # One by one extract an element
    # from heap
    for i in range(n-1, -1, -1):
         
        # Move current root to end #
        arr[0], arr[i] = arr[i], arr[0]
        draw_list(draw_info,{i:draw_info.GREEN, 0:draw_info.RED}, True)
        yield True
        heapify(draw_info,arr, i, 0)

# non comparison based sorting wala part
def merge(bar, left, mid, right, win):
    temp = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        bar[i].check()
        bar[j].check()
        draw(win, bar)
        bar[i].back()
        bar[j].back()
        if bar[i].value < bar[j].value:
            temp.append(bar[i])
            i += 1
        else:
            temp.append(bar[j])
            j += 1
    while i <= mid:
        bar[i].check()
        draw(win, bar)
        bar[i].back()
        temp.append(bar[i])
        i += 1
    while j <= right:
        bar[j].check()
        draw(win, bar)
        bar[j].back()
        temp.append(bar[j])
        j += 1
    k = 0
    for i in range(left, right + 1):
        bar[i] = temp[k]
        bar[i].reset(i)
        bar[i].check()
        draw(win, bar)
        if right - left == len(bar) - 1:
            bar[i].done()
        else:
            bar[i].back()
        k += 1


def merge_sort(bar, left, right, win):
    # Set global variables to control
    # the quitting function and shuffle function for the list
    # before running
    global SORTED
    SORTED = True
    global RUN

    mid = left + (right - left) // 2
    if left < right:
        merge_sort(bar, left, mid, win)
        merge_sort(bar, mid + 1, right, win)
        if not RUN:
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                break
        merge(bar, left, mid, right, win)

def count_sort(arr):
    start = time.time()
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    # Create a count array to store count of individual
    # elements and initialize count array as 0
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]
  
    # Store count of each character
    for i in range(0, len(arr)):
        count_arr[arr[i]-min_element] += 1
  
    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
  
    # Build the output character array
    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1
  
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]
    end = time.time()
    return end- start
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
                  # slot's size is 0.1
    for i in range(slot_num):
        arr.append([])
          
    # Put array elements in different buckets 
    for j in x:
        index_b = int(slot_num * j) 
        arr[index_b].append(j)
      
    # Sort individual buckets 
    for i in range(slot_num):
        arr[i] = insertionSort_bucket(arr[i])
          
    # concatenate the result
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

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
def radixSort(array):
    start = time.time()
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort_radix(array, place)
        place *= 10
    end = time.time()
    return end-start


def main():
    
    read = open(ui_main(), "r")
    score_list = read.read().split(',');
    float_list = []
    int_list = []
    for i in range(len(score_list)):
        float_list.append(float(score_list[i][1:]))
    for i in range(len(score_list)):
        int_list.append(int(score_list[i][1:]))
    print("Do you want to see comparison or non-comparison based sort? \n1. Comparision sorts \n2. Non Comparision sort")
    choice = int(input())
  
    if choice ==1:	
        run = True
        clock = pygame.time.Clock()
        n=50
        min_val = 0
        max_val = 100
        sorting = False
        ascending = True
        sorting_algorithm = bubble_sort
        sorting_algorithm_name = "Bubble Sort"
        sorting_algorithm_generator = None
        lst = generating_starting_list(n, min_val, max_val)
        draw_info = DrawInformation(1200, 800, lst)
        while run: 
            # fps
            clock.tick(60)
            if sorting:
                try:
                    next(sorting_algorithm_generator)
                except StopIteration:
                    sorting = False
            else: 
                draw(draw_info, sorting_algorithm_name, ascending)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type != pygame.KEYDOWN: # pressing key down 
                    continue
                if event.key == pygame.K_r: #pressing key R
                    lst = generating_starting_list(n, min_val, max_val)
                    draw_info.set_list(lst)
                    sorting = False
                elif event.key == pygame.K_SPACE and sorting==False:
                    sorting= True
                    sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
                elif event.key == pygame.K_a and not sorting:
                    ascending = True
                elif event.key == pygame.K_d and not sorting:
                    ascending = False
                elif event.key == pygame.K_s and not sorting:
                    sorting_algorithm = selection_sort
                    sorting_algorithm_name = "Selection Sort"
                elif event.key == pygame.K_b and not sorting:
                    sorting_algorithm = bubble_sort
                    sorting_algorithm_name = "Bubble Sort"
                elif event.key == pygame.K_i and not sorting:
                    sorting_algorithm = insertion_sort
                    sorting_algorithm_name = "Insertion Sort"
                elif event.key == pygame.K_h and not sorting:
                    sorting_algorithm_name = "Heap Sort"
                    if (ascending==False):
                        heapSort_descending(draw_info, ascending)
                    else:
                        heapSort(draw_info, ascending)
                elif event.key == pygame.K_q and not sorting:
                    sorting_algorithm = insertion_sort
                    sorting_algorithm_name = "Quick Sort"
                
                
        pygame.quit()
    else:
        main_code(float_list, int_list)
        
        
if __name__ == "__main__":
    main()




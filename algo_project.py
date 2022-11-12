import pygame
import random
import math
pygame.init()

class DrawInformation:
	BLACK = 0, 0, 0
	WHITE = 255, 255, 255
	GREEN = 0, 255, 0
	RED = 255, 0, 0
	BACKGROUND_COLOR = WHITE
	BLUE = 0, 0, 255
	GRADIENTS = [
		(128, 128, 128),
		(160, 160, 160),
		(192, 192, 192)
	]

	FONT = pygame.font.SysFont('Times New Roman', 30)
	LARGE_FONT = pygame.font.SysFont('comicsans', 40)

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
	title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.BLACK)
	draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2, 1))

	# font rendered
	controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, draw_info.BLUE)
	# display it on the screen
	draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2, 55))
	# sorting wala part display
	sorting = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort | S - Selection Sort | H - Heap Sort", 1, draw_info.BLUE)
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
def buildMaxHeap(draw_info, ascending, lst):
    n = len(lst)
    for i in range(n):
         
        # if child is bigger than parent
        if lst[i] > lst[int((i - 1) / 2)]:
            j = i
     
            # swap child and parent until
            # parent is smaller
            while lst[j] > lst[int((j - 1) / 2)]:
                (lst[j],lst[int((j - 1) / 2)]) = (lst[int((j - 1) / 2)],lst[j])
                draw_list(draw_info, {int((j - 1) / 2): draw_info.GREEN, j:draw_info.RED})
                yield True
                j = int((j - 1) / 2)
 
def heapSort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)
    buildMaxHeap(draw_info, ascending, lst)
 
    for i in range(n - 1, 0, -1):
         
        # swap value of first indexed
        # with last indexed
        lst[0], lst[i] = lst[i], lst[0]
        draw_list(draw_info, {0:draw_info.GREEN, i:draw_info.RED})
        yield True
        # maintaining heap property
        # after each swapping
        j, index = 0, 0
         
        while True:
            index = 2 * j + 1
             
            # if left child is smaller than
            # right child point index variable
            # to right child
            if (index < (i - 1) and
                lst[index] < lst[index + 1]):
                index += 1
         
            # if parent is smaller than child
            # then swapping parent with child
            # having higher value
            if index < i and lst[j] < lst[index]:
                lst[j], lst[index] = lst[index], lst[j]
                draw_list(draw_info, {index: draw_info.GREEN, j: draw_info.RED})
         
            j = index
            if index >= i:
                break

def main():
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
				sorting_algorithm = heapSort
				sorting_algorithm_name = "Heap Sort"
			
	pygame.quit()
if __name__ == "__main__":
	main()




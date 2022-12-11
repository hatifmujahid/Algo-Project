from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time

ws = Tk()
ws.title('Array file input UI')
ws.geometry('600x600') 



def choose_option(i):
    global choice
    choice = i
    Label(ws, text='Choice selected successfully', foreground='green').grid(row=4, columnspan=3, pady=10)
    time.sleep(2)
    ws.destroy()
    
adhar = Label(
    ws, 
    text='Choose option: '
    )
adhar.grid(row=0, column=0, padx=10)

adharbtn = Button(
    ws, 
    text ='1. SORTING VISUALIZED(small file)', 
    command = lambda:choose_option(1)
    ) 
adharbtn.grid(row=10, column=1)

adharbtn2 = Button(
    ws, 
    text ='2. N-TIME GRAPH OF ALGORITHMS(randoms file)', 
    command = lambda:choose_option(2)
    ) 
adharbtn2.grid(row=12, column=1)



def ui_choice():
    ws.mainloop()
    return choice
ui_choice()
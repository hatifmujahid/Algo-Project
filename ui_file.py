from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time

ws = Tk()
ws.title('Array file input UI')
ws.geometry('400x400') 


def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Text Files', '*txt')])
    global x
    x = file_path.name
    if file_path is not None:
        pass

def uploadFiles():
    pb1 = Progressbar(
        ws, 
        orient=HORIZONTAL, 
        length=300, 
        mode='determinate',

        )
    pb1.grid(row=4, columnspan=3, pady=20, padx= 20)
    for i in range(5):
        ws.update_idletasks()
        pb1['value'] += 20
        time.sleep(0.2)
    pb1.destroy()
    Label(ws, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)
    ws.destroy()
        
    
    
adhar = Label(
    ws, 
    text='Upload array file'
    )
adhar.grid(row=0, column=0, padx=10)

adharbtn = Button(
    ws, 
    text ='Choose File', 
    command = lambda:open_file()
    ) 
adharbtn.grid(row=0, column=1)


upld = Button(
    ws, 
    text='Upload Files', 
    command=uploadFiles
    )
upld.grid(row=3, columnspan=3, pady=10)


def ui_main():
    ws.mainloop()
    return x
ui_main()
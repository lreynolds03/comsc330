# !!!!!!! for running, add 'if name == "main":' above the 'main()' in run_class.py. !!!!!!

import tkinter as tk
from tkinter import *
from tkinter import filedialog # filegetter & listbox
from tkinter import messagebox # warning message
from tkinter import scrolledtext # conlsole box

import run_class
import os # to get the list of files in a directory

dir = None # variable, store the path of the directory
file_list = [] # list, store the files

def fileGetter(): #btn1
    dir = filedialog.askdirectory(initialdir = "./", title = "Select a directory")
    
    if dir == '':
        messagebox.showwarning("Warning", "No directory selected")
        
        log = "No directory has loaded.\n"
        ResultViewlabel_ScrollBox.insert(tk.END, log)
    else:
        run_file = os.listdir(dir) # get the list of files in the directory
        runlist.delete(0, tk.END) # clear listbox
        
        log = f"['{dir}'] has loaded.\n"
        ResultViewlabel_ScrollBox.insert(tk.END, log)
        
        for file in run_file:
            if file.endswith(".run"): # only add .run files on the listbox
                runlist.insert(tk.END, file)

def fileSetter(): # btn2
    selection = runlist.curselection() # get the selected file
    
    if selection:
        selected_file = runlist.get(selection[0]) # get the name of the file
        
        with open('results.txt', 'w') as outFile: # open a file to write the results (at run_class.py)
            run_class.run(selected_file, outFile) # run file
            
        log = f"Successfully ran {selected_file}\n"
        ResultViewlabel_ScrollBox.insert(tk.END, log)

def closing(): #btn3
    root.destroy() # exit window

root = tk.Tk() # create a window
root.geometry("272x170") # set the size
root.attributes('-topmost', True) # keep the window on top
root.resizable(False, False) # disable resizing
root.overrideredirect(True) # remove the title bar

runlist = Listbox(root, width = 20, height = 5) # listbox
runlist.place(x = 5, y = 10)

btn1 = Button(root, text = "Load", fg = "red", comman = fileGetter, width = 5, height = 1) # button(Load)
btn1.place(x = 190, y = 7)

btn2 = Button(root, text = "Calculate", fg = "blue", command = fileSetter, width = 5, height = 1) # button(Clac)
btn2.place(x = 190, y = 37)

btn3 = Button(root, text = "Exit", fg = "green", command = closing, width = 5, height = 1) # button(Exit)
btn3.place(x = 190, y = 67)

ResultViewlabel_ScrollBox = scrolledtext.ScrolledText(width = 34, height = 4, wrap = tk.WORD, font = ('Normal', 11)) # console box
ResultViewlabel_ScrollBox.place(x = 3, y = 100)

root.mainloop() # run

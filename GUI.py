# !!!!!!! for running, add 'if __name__=="__main__":' above the 'main()' in run_class.py. !!!!!!
# !!!!!!! if you wanna test with this code, go terminal and enter 'brew install python3-tk' !!!!!
import tkinter as tk
from tkinter import * # to make GUI
from tkinter import filedialog # to open a dialog to select a directory
from tkinter import messagebox # to show a warning message
from tkinter import scrolledtext # to create a scrollable text box

from organization import organization # to use organization(Student Grade Breakdown)

import run_class
import os # to get the list of files in a directory

# --------------------- Variables ---------------------
dir = None # Variable, to store the path of the directory
file_list = [] # List, to store the files

# -------------------- GUI Window ---------------------
root = tk.Tk() # Create a window

root.geometry("272x170") # Set the size of the window
root.attributes('-topmost', True) # Keep the window on top
root.resizable(False, False) # Disable resizing of the window
root.overrideredirect(True) # Remove the title bar

# --------------------- List Box ----------------------
runlist = Listbox(root, width = 20, height = 5) # Create a listbox

runlist.place(x = 5, y = 10)

# -------------- Get file list(Button1) ---------------
def fileGetter():
    dir = filedialog.askdirectory(title = "Select a directory") # Open a dialog to select a directory
    
    if dir == '':
        messagebox.showwarning("Warning", "No directory selected")
        
        log = "No directory has loaded.\n"
        ResultViewlabel_ScrollBox.insert(tk.END, log)
    else:
        run_file = os.listdir(dir) # Get the list of files in the directory
        runlist.delete(0, tk.END) # Clear the listbox
        
        log = f"['{dir}'] has loaded.\n"
        ResultViewlabel_ScrollBox.insert(tk.END, log)
        
        for file in run_file:
            if file.endswith(".run"): # Only add .run files on the listbox
                runlist.insert(tk.END, file)

# --------------------- Button(1) ---------------------
btn1 = Button(root, text = "Load", fg = "red", comman = fileGetter, width = 5, height = 1) # Create a button

btn1.place(x = 190, y = 7)

# -------------- Set file list(Button2) ---------------
def breakdown(outFile, temp, des): # to write grade breakdown
    if len(temp) == 0: # if there is no student(temp: grade list)
        outFile.write(f'\nNo students with {des}') # des: range for grade
    else:
        outFile.write(f'\nStudents with {des}: ')
        for row in temp:
            outFile.write('\n')
            for count, info in enumerate(row):
                if count == 0:
                    outFile.write(f'{info}: ')
                else:
                    outFile.write(f'\t{info}')
        outFile.write('\n')

def fileSetter():
    selection = runlist.curselection()  # Get the selected file

    if selection:
        selected_file = runlist.get(selection[0])  # Get the name of the selected file
        all = [] # have to be [] (to use list)

        with open('results.txt', 'w') as outFile:  # Open a file to write the results
            results = run_class.run(selected_file, outFile, all)  # Run the selected file

            # call the organization
            A, D = organization(results)
            outFile.write('Student Grade Breakdown:\n')
            breakdown(outFile, A, "more than one A or A-")
            breakdown(outFile, D, "more than one D-, D, D+, or F")

        log = f"Successfully ran {selected_file}\n"
        ResultViewlabel_ScrollBox.insert(tk.END, log)

# --------------------- Button(2) ---------------------
btn2 = Button(root, text = "Calculate", fg = "blue", command = fileSetter, width = 5, height = 1) # Create a button

btn2.place(x = 190, y = 37)

# --------------- Close window(Button3) ---------------
def closing():
    root.destroy() # Close the window

# --------------------- Button(3) ---------------------
btn3 = Button(root, text = "Exit", fg = "green", command = closing, width = 5, height = 1) # Create a button

btn3.place(x = 190, y = 67)

# ------------------- Result Console ------------------
ResultViewlabel_ScrollBox = scrolledtext.ScrolledText(width = 34, height = 4, wrap = tk.WORD, font = ('Normal', 11)) # Create a console for log
ResultViewlabel_ScrollBox.place(x = 3, y = 100)

root.mainloop() # Run the window

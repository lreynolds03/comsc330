"""
GRP file class

Read in grp file 
Run SEC class for each SEC file 
"""

from sec_class import sec
#import math_class

def grp(grpFile, outFile):

    with open(grpFile, 'r') as file:
        f = file.read()
    
    f = f.replace('\n', ',') # replaces each new line symbol with a comma
    f = f.split(',') # splits each element between commas

    sec_array = []

    for i in range(1, len(f)-1):
        sec_array.append(f[i]) # creates array full of .sec files

    print(sec_array)

    for file in range(0, len(sec_array)):
        sec(sec_array[file], outFile) # runs sec class for every .sec file in array

"""
def main():

    file = input('Enter the name of the file you want to run: ')
    print('\n')
    grp(file)

main()
"""

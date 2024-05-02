"""
GRP file class

Read in grp file 
Run SEC class for each SEC file 
"""

from sec_class import sec

def grp(grpFile, outFile, all): # grpFile is the file name of the group file

    with open(grpFile, 'r') as file:
        f = file.read()
    
    f = f.replace('\n', ',') # replaces each new line symbol with a comma
    f = f.split(',') # splits each element between commas

    sec_array = [] # array to store sec files

    for i in range(1, len(f)-1):
        sec_array.append(f[i]) # creates array full of .sec files

    # print(sec_array)

    for file in range(0, len(sec_array)):
        outFile.write(str(sec_array[file][0:-4])) # writes name of .grp file to results.txt
        outFile.write(', GPA: \n')
        results = sec(sec_array[file], outFile, all) # runs sec class for every .sec file in array
        all.append(results)

    outFile.write('\n')

    return all

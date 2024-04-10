"""
SEC files class

Read in a section file
return 2D array
"""

import re   # necessary to remove quotes from student info

def sec(secFile, outFile):

    with open (secFile, 'r') as file:
        f = file.read()

    f = f.replace('"', '') # replacing quotation marks with blank space
    f = f.replace('\n', ',') # replaces each new line symbol with a comma
    f = f.split(',') # splits each element between commas

    studentInfo = []
    studentInfo.append(f[0]) # puts course name and credit hours as first element of array

    for i in range(1, len(f)-1, 4): 
        studentInfo.append(f[i:i+4]) # Groups four items at a time starting at first students last name  

    # return array of student info

"""
def main():

    file = input('Enter the name of the file you want to run: ')
    sec(file)

main()
"""

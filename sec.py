"""
SEC files class

Read in a section file
return 2D array
"""

import re   # necessary to remove quotes from student info

def sec(secFile):

    with open (secFile, 'r') as file: # Opens file
        f = file.read() # reads in entire file into f

    f = f.replace('"', '') # replacing quotation marks with blank space
    f = f.replace('\n', ',') # replaces each new line symbol with a comma
    f = f.split(',') # splits each element between commas

    studentInfo = [] # initialize array 
    studentInfo.append(f[0]) # puts course name and credit hours as first element of array

    for i in range(1, len(f), 4): 
        studentInfo.append(f[i:i+4]) # Appends 

    """
    For loop to print out each student info 
    
    for i in range(1, len(studentInfo)-1):
        print(studentInfo[i][3])
        print('\n')

    print(studentInfo[0])
    """

    # return array of student info
    return studentInfo 

"""
Testing the class with section file
def main():

    file = input('Enter the name of the file you want to run: ')
    sec(file)

main()
"""

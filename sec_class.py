"""
SEC files class

Read in a section file
return 2D array
"""

import re   # necessary to remove quotes from student info


def sec(secFile, outFile, tempMulti): # secFile is the file name of the section file

    with open (secFile, 'r') as file:
        f = file.read()

    f = f.replace('"', '') # replacing quotation marks with blank space
    f = f.replace('\n', ',') # replaces each new line symbol with a comma
    f = f.split(',') # splits each element between commas

    ch = f[0][-3:] 
    course = f[0][0:-6]

    temp = []
    temp.append(course)
    temp.append(ch)
    print(temp)


    studentInfo = []
    studentInfo.append(temp)

    for i in range(1, len(f)-1, 4): # i = 1-4, 5-8, 9-12, etc.
        studentInfo.append(f[i:i+4]) # Groups four items at a time starting at first students last name  

    import calculations as c

    # call calculation class
    results = c.mainGPA(studentInfo, tempMulti)
    r = results[2:]
    return r


'''
def main():

    file = input('Enter the name of the file you want to run: ')
    outFile = 0
    tempMulti = []
    sec(file, outFile, tempMulti)

main()

'''
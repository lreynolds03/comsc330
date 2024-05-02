"""
GRP file class

Read in grp file 
Run SEC class for each SEC file 
"""

from sec_class import sec
#import math_class
def grp(grpFile, outFile, all): # grpFile is the file name of the group file

    with open(grpFile, 'r') as file:
        f = file.read()
    
    f = f.replace('\n', ',') # replaces each new line symbol with a comma
    f = f.split(',') # splits each element between commas

    sec_array = [] # array to store sec files

    for i in range(1, len(f)-1):
        sec_array.append(f[i]) # creates array full of .sec files

    print(sec_array)

    sectionAverage = []

    for file in range(0, len(sec_array)):
        results = sec(sec_array[file], outFile, sectionAverage, all) # runs sec class for every .sec file in array
        sectionAverage.append(results[0])
        significant = results[1]
        all.append(results[2])

    import calculations as c
    import array as a
    count = 0
    ch = 0
    section = []


    for x in sectionAverage:
        count =count+1
        if count%3 == 1:
            # append credit hours
            ch = ch+1
        elif count%3 == 2:
            # append average section GPA
            section.append(x)

    count = 0
    for file in range(0, len(sec_array)):
        outFile.write('\t')
        outFile.write(str(sec_array[file][0:-4]))  # writes name of .grp file to results.txt
        outFile.write(', GPA: \t')
        outFile.write(str('%.2f'%section[count]))
        outFile.write('\n')
        count = count+1

    outFile.write('\n')

    from array import array
    section = array('f', section)
    groupAverage = c.calcAverageGPA(ch, section)
    value = c.signif(groupAverage, section, significant)

    return all, value, groupAverage, ch

"""
def main():

    file = input('Enter the name of the file you want to run: ')
    print('\n')
    grp(file)

main()
"""




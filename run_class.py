"""
RUN class
"""
from grp_class import grp
import re # necessary to remove quotes from student info

def run(runFile, outFile, all): # runFile is the file name of the run file

    # open file input by user
    with open(runFile, 'r') as file:
        f = file.read()

    f = f.replace('\n', ',') # replaces each new line symbol with a comma
    f = f.split(',') # splits each element between commas

    grp_array = []

    for i in range(1, len(f)):
        grp_array.append(f[i]) # creates array full of .grp files

    print(grp_array)

    groupGPA = []
    for grpFile in range(0, len(grp_array)):
        outFile.write(str(grp_array[grpFile])) # writes name of .grp file to results.txt
        outFile.write('\n')
        results = grp(grp_array[grpFile], outFile, all) # runs grp class for every .grp file in array
        all = results[0]
        significant = results[1]
        groupAverage = results[2]
        ch = results[3]
        groupGPA.append(groupAverage)

    import calculations as c
    from array import array
    groupGPA = array('f', groupGPA)
    print(ch)
    groupAverage = c.calcAverageGPA(ch, groupGPA)
    significant = c.signif(groupAverage, groupGPA, significant)
    if len(significant)<1:
        outFile.write("There are no significant values \n")
    else:
        count = 0
        for x in significant:
            outFile.write("There is a significant value at this GPA: ")
            outFile.write(str(x))
            outFile.write('\n')
    return all

def main():
    file = input(
        'Enter the name of the .run file you want to run (ex: filename.run), or type \'quit\' to exit program:\n')

    # create results text file
    with open('results.txt', 'w') as results:

        all = []
        r = run(file, results, all)

        from organization import organization
        number = organization(r)
        count = 0
        for element in number:
            count = count + 1
            if count == 1:
                A = element
            elif count == 2:
                D = element

        results.write('Student Grade Breakdown:\n')

        if len(A) == 0:
            results.write('\nNo students with more than one A or A-')
        elif len(A) > 0:
            results.write('\nStudents with more than one A or A-: ')
            for row in A:
                count = 0
                for element in row:
                    if count == 1:
                        results.write('\n')
                        results.write(str(element))
                        results.write(': ')
                    elif count >= 2:
                        results.write('\t')
                        results.write(str(element))
                    count = count + 1
            results.write('\n')

        if len(D) == 0:
            results.write('\nNo students with more than one D-, D, D+, or F')
        elif len(D) > 0:
            results.write('\nStudents with more than one D-, D, D+, or F: ')
            for row in D:
                count = 0
                for element in row:
                    if count == 1:
                        results.write('\n')
                        results.write(str(element))
                        results.write(': ')
                    elif count >= 2:
                        results.write('\t')
                        results.write(str(element))
                    count = count + 1
            results.write('\n')

    results.close()


main()
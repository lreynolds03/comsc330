"""
RUN class
"""

from grp_class import grp

def run(runFile, outFile, all): # runFile is the file name of the run file

    # open file input by user
    with open(runFile, 'r') as file:
        f = file.read()

    f = f.replace('\n', ',') # replaces each new line symbol with a comma
    f = f.split(',') # splits each element between commas

    grp_array = []

    for i in range(1, len(f)):
        grp_array.append(f[i]) # creates array full of .grp files

    for grpFile in range(0, len(grp_array)):
        outFile.write('Group:\t')
        outFile.write(str(grp_array[grpFile][0:-4])) # writes name of .grp file to results.txt
        outFile.write('\nGroup GPA: \n')
        results = grp(grp_array[grpFile], outFile, all) # runs grp class for every .grp file in array

    return results

def main():
# def main(file): # !!!!!! relplace upper line and delete under line if run it through GUI.py !!!!!!
    file = input('Enter the name of the .run file you want to run (ex: filename.run), or type \'quit\' to exit program:\n')

        # create results text file
    with open ('results.txt', 'w') as results:
        
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
            results.write('\nNo students with more than one D-, D, D+, or F')
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
                    count = count+1
            results.write('\n')

    results.close()

# if __name__=="__main__": # !!!!!! add this line and insert TAB under line if run it through GUI.py !!!!!!
main()

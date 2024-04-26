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


    for grpFile in range(0, len(grp_array)):
        outFile.write(str(grp_array[grpFile])) # writes name of .grp file to results.txt
        outFile.write('\n')
        results = grp(grp_array[grpFile], outFile, all) # runs grp class for every .grp file in array
    return results

def main():

    file = input('Enter the name of the .run file you want to run (ex: filename.run), or type \'quit\' to exit program:\n')

        # create results text file
    with open ('results.txt', 'w') as results:
        while file != 'quit': # loop to run program until user types 'quit'
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
                    AMinus = element
                elif count == 3:
                    DPlus = element
                elif count == 4:
                    D = element
                elif count == 5:
                    DMinus = element
                elif count == 6:
                    F = element

            print('A: ', A)
            print('AMinus: ', AMinus)
            print('DPlus: ', DPlus)
            print('D: ', D)
            print('DMinus: ', DMinus)
            print('F', F)

            results.write('\nStudents with more than one A: ')
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
            results.write('\nStudents with more than one A-: ')
            for row in AMinus:
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
            results.write('\nStudents with more than one D+: ')
            for row in DPlus:
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
            results.write('\nStudents with more than one D: ')
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
            results.write('\nStudents with more than one D-: ')
            for row in DMinus:
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
            results.write('\nStudents with more than one F: ')
            for row in F:
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


            file = input('Enter the name of the .run file you want to run (ex: filename.run), or type \'quit\' to exit program:\n')

            if file == 'quit':

                results.close()

main()
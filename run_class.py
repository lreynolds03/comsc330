"""
RUN class
"""

from grp_class import grp
import re # necessary to remove quotes from student info

def run(runFile, outFile): # runFile is the file name of the run file

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
        grp(grp_array[grpFile], outFile) # runs grp class for every .grp file in array

def main():

    file = input('Enter the name of the .run file you want to run (ex: filename.run), or type \'quit\' to exit program:\n')

        # create results text file
    with open ('results.txt', 'w') as results:
        while file != 'quit': # loop to run program until user types 'quit'

            run(file, results)

            file = input('Enter the name of the .run file you want to run (ex: filename.run), or type \'quit\' to exit program:\n')

            if file == 'quit':
                results.close()

main()

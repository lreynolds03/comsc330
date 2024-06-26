import math

# calculates GPA of given section
def GPA(ID, course, s, ch, individualGPA, successDict, failDict, sumPoints):
    group = {}
    if s == 'A':
        # calculate GPA given credit hours
        gpa = ch * 4.0
        individualGPA.append(4.0)
        sumPoints = gpa + sumPoints

        # use dictionary to track students with more than one A or A-
        if successDict.fromkeys(ID) == True:
            successDict[ID].add(course)
        else:
            successDict.update({ID: course})


        return gpa, individualGPA, successDict, failDict, sumPoints
    elif s == 'A-':
        gpa = ch * 3.7
        individualGPA.append(3.7)
        sumPoints = gpa + sumPoints
        # use dictionary to track students with more than one A or A-
        # use dictionary to track students with more than one A or A-

        if successDict.fromkeys(ID) == True:
            successDict[ID].add(course)
        else:
            successDict.update({ID: course})

        return gpa, individualGPA, successDict, failDict, sumPoints
    elif s == 'B+':
        gpa = ch * 3.3
        individualGPA.append(3.3)
        sumPoints = gpa + sumPoints
        return gpa, individualGPA, successDict, failDict, sumPoints
    elif s == 'B':
        gpa = ch * 3.0
        individualGPA.append(3.0)
        sumPoints = gpa + sumPoints
        return gpa, individualGPA, successDict, failDict, sumPoints
    elif s == 'B-':
        gpa = ch * 2.7
        individualGPA.append(2.7)
        sumPoints = gpa + sumPoints
        return gpa, individualGPA, successDict, failDict, sumPoints
    elif s == 'C+':
        gpa = ch * 2.3
        individualGPA.append(2.3)
        sumPoints = gpa + sumPoints
        return gpa, individualGPA, successDict, failDict, sumPoints
    elif s == 'C':
        gpa = ch * 2.0
        individualGPA.append(2.0)
        sumPoints = gpa + sumPoints
        return gpa, individualGPA, successDict, failDict, sumPoints
    elif s == 'C-':
        gpa = ch * 1.7
        individualGPA.append(1.7)
        sumPoints = gpa + sumPoints
        return gpa, individualGPA, successDict, failDict, sumPoints
    elif s == 'D+':
        gpa = ch * 1.3
        individualGPA.append(1.3)
        sumPoints = gpa + sumPoints

        # use dictionary to track students with more than one D+, D, D-, or F
        if failDict.fromkeys(ID) == True:
            failDict[ID].add(course)
        else:
            failDict.update({ID: course})

        return gpa, individualGPA, successDict, failDict, sumPoints
    elif s == 'D':
        gpa = ch * 1.0
        individualGPA.append(1.0)
        sumPoints = gpa + sumPoints

        # use dictionary to track students with more than one D+, D, D-, or F
        if failDict.fromkeys(ID) == True:
            failDict[ID].add(course)
        else:
            failDict.update({ID: course})

        return gpa, individualGPA, successDict, failDict, sumPoints
    elif s == 'D-':
        gpa = ch * 0.7
        individualGPA.append(0.7)
        sumPoints = gpa + sumPoints

        # use dictionary to track students with more than one D+, D, D-, or F
        # use dictionary to track students with more than one A or A-
        # use dictionary to track students with more than one D+, D, D-, or F
        if failDict.fromkeys(ID) == True:
            failDict[ID].add(course)
        else:
            failDict.update({ID: course})

        return gpa, individualGPA, successDict, failDict, sumPoints
    elif s == 'F':
        gpa = ch * 0
        individualGPA.append(0)
        sumPoints = gpa + sumPoints

        # use dictionary to track students with more than one D+, D, D-, or F
        if failDict.fromkeys(ID) == True:
            failDict[ID].add(course)
        else:
            failDict.update({ID: course})

        return gpa, individualGPA, successDict, failDict, sumPoints
    # line allows code to disregard grade letters not mentioned above (ie "I" or "W")
    else:
        gpa = 'NA'
        return gpa, individualGPA, successDict, failDict




    # calculate average GPA
def calcAverageGPA(hours, sumPoints):
    average = sumPoints / hours
    return average


def zScore(average, gpa, sd):
    # for each gpa in file calculate z score
    z = (gpa - average) / sd
    return z

def difOfSquares(average, gpa, sum):
    # for each gpa in file
    difference = abs(gpa) - average
    sqdif = difference * difference
    sum += sqdif
    return sum
    # end
def mainGPA(array, successDict, failDict):
    # initialize variables
    totalHours = 0
    sumPoints = 0.0
    sum = 0
    course = ''
    ch = 0

    # array of unweighted GPA values
    individualGPA = []
    significant = []

    results = 0
    # calculates gpas of each student given a section array
    tally = 0
    for row in array:
        tally = tally + 1
        print(row)
        # Resets count after each row

        countRow = 0
        if tally == 1:
            for val in row:
                countRow = countRow + 1
                if countRow == 1:
                    course = val
                elif countRow == 2:
                    ch = float(val)
        else:
            for val in row:
                countRow += 1
                # If count = 3, value is the students ID
                if countRow == 3:
                    ID = val
                # If count = 4, grade letter
                elif countRow == 4:
                    s = val
            results = GPA(ID, course, s, ch, individualGPA, successDict, failDict, sumPoints)
            totalHours = totalHours+ch

    individualGPA = results[1]
    successDict = results[2]
    failDict = results[3]
    sumPoints = results[4]

    # calculates gpa of using the given credit hours and grade letter

    average = calcAverageGPA(totalHours, sumPoints)

    # calculates difference of sums
    for val in individualGPA:
        sum += difOfSquares(average, val, sum)

    # calculate standard deviation (square root of sum/n-1)

    sd = math.sqrt(sum / (len(individualGPA)- 1))

    # calculate zscore for each element in gpa Array
    for val in individualGPA:
        z = zScore(average, val, sd)
        # print element if zscore is significant
        if (z<=-2) or (z>=2):
            significant.append("\n",val, "is significant with a zscore of: ", z)
            print(val, "is significant with a zscore of: ", z)


    # print output of program
    print("success: ", successDict)
    print('fail: ', failDict)

    return average, successDict, failDict, significant
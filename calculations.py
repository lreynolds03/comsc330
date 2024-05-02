import math

def add(s, ID, course, tempMulti):
    count = 0
    array = []
    # Checks if tempMulti is empty
    if len(tempMulti) == 0:
        # adds in a new array with students:
        # grade
        array.insert(0, s)
        # ID
        array.insert(1, ID)
        # and Course
        array.insert(2, course)
        # appends array to main, tempMulti
        tempMulti.append(array)
    else:
        sCount = 0
        idCount = 0
        # check each student info in current array
        for row in tempMulti:
            # check if student ID is already in array
            if row[0] == s:
                # if so, increase count to indicate already in array
                sCount = sCount+1
                if row[1] == ID:
                    idCount = idCount+1
                    for val in row:
                        if val == course:
                            count = count+1
                    if count < 1:
                        row.append(course)


        if idCount <1:
            if sCount <1:
                array.insert(0,s)
                array.insert(1,ID)
                array.insert(2,course)
                tempMulti.append(array)
            else:
                array.insert(0,s)
                array.insert(1,ID)
                array.insert(2,course)
                tempMulti.append(array)



    return tempMulti



# calculates GPA of given section
def GPA(ID, course, s, ch, individualGPA, tempMulti, sumPoints):
    if s == 'A':
        # calculate GPA given credit hours
        gpa = ch * 4.0
        individualGPA.append(4.0)
        sumPoints = gpa + sumPoints

        tempMulti = add(s, ID, course, tempMulti)


        return gpa, individualGPA, tempMulti, sumPoints
    elif s == 'A-':
        gpa = ch * 3.7
        individualGPA.append(3.7)
        sumPoints = gpa + sumPoints
        # use dictionary to track students with more than one A or A-
        tempMulti = add(s, ID, course, tempMulti)

        return gpa, individualGPA, tempMulti, sumPoints
    elif s == 'B+':
        gpa = ch * 3.3
        individualGPA.append(3.3)
        sumPoints = gpa + sumPoints
        return gpa, individualGPA, tempMulti, sumPoints
    elif s == 'B':
        gpa = ch * 3.0
        individualGPA.append(3.0)
        sumPoints = gpa + sumPoints
        return gpa, individualGPA, tempMulti, sumPoints
    elif s == 'B-':
        gpa = ch * 2.7
        individualGPA.append(2.7)
        sumPoints = gpa + sumPoints
        return gpa, individualGPA, tempMulti, sumPoints
    elif s == 'C+':
        gpa = ch * 2.3
        individualGPA.append(2.3)
        sumPoints = gpa + sumPoints
        return gpa, individualGPA, tempMulti, sumPoints
    elif s == 'C':
        gpa = ch * 2.0
        individualGPA.append(2.0)
        sumPoints = gpa + sumPoints
        return gpa, individualGPA, tempMulti, sumPoints
    elif s == 'C-':
        gpa = ch * 1.7
        individualGPA.append(1.7)
        sumPoints = gpa + sumPoints
        return gpa, individualGPA, tempMulti, sumPoints
    elif s == 'D+':
        gpa = ch * 1.3
        individualGPA.append(1.3)
        sumPoints = gpa + sumPoints
        tempMulti = add(s, ID, course, tempMulti)

        return gpa, individualGPA, tempMulti, sumPoints
    elif s == 'D':
        gpa = ch * 1.0
        individualGPA.append(1.0)
        sumPoints = gpa + sumPoints
        tempMulti = add(s, ID, course, tempMulti)

        return gpa, individualGPA, tempMulti, sumPoints
    elif s == 'D-':
        gpa = ch * 0.7
        individualGPA.append(0.7)
        sumPoints = gpa + sumPoints
        tempMulti = add(s, ID, course, tempMulti)

        return gpa, individualGPA, tempMulti, sumPoints
    elif s == 'F':
        gpa = ch * 0
        individualGPA.append(0)
        sumPoints = gpa + sumPoints
        tempMulti = add(s, ID, course, tempMulti)

        return gpa, individualGPA, tempMulti, sumPoints
    # line allows code to disregard grade letters not mentioned above (ie "I" or "W")
    else:
        gpa = 'NA'
        return gpa, individualGPA, tempMulti, sumPoints




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

def signif(average, array, significant):
    print (array)
    print (significant)
    # initialize sum
    sum = 0

    # calculates difference of sums
    for val in array:
        sum += difOfSquares(average, val, sum)

    # calculate standard deviation (square root of sum/n-1)

    sd = math.sqrt(sum / (len(array) - 1))

    # calculate zscore for each element in gpa Array
    for val in array:
        z = zScore(average, val, sd)
        # print element if zscore is significant
        if (z <= -2) or (z >= 2):
            significant.append(val)
            significant(z)

    return significant

def mainGPA(array, tempMulti):
    # initialize variables
    totalHours = 0
    sumPoints = 0.0
    course = ''
    ch = 0
    # array of unweighted GPA values
    individualGPA = []
    significant = []

    results = 0

    # calculates gpas of each student given a section array
    count = 0
    for row in array:
        count = count+1
        if count == 1:
            course = row[0]
            ch = float(row[1])


        else:
            # determines length of the given array
            length = len(row)

            # determines specific informatoin about student

            # ID is always second to last position
            ID = row[length-2]
            # s is always last position
            s = row[length-1]

            results = GPA(ID, course, s, ch, individualGPA, tempMulti, sumPoints)
            totalHours = totalHours + ch




    individualGPA = results[1]
    tempMulti = results[2]
    sumPoints = results[3]

    # calculates gpa of using the given credit hours and grade letter

    average = calcAverageGPA(totalHours, sumPoints)

    significant = signif(average, individualGPA, significant)

    return average, significant, tempMulti
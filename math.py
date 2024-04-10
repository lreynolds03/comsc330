import math
from collections import Counter

# testing variables
s = "A"
totalHours = 0
sumPoints = 0.0
ch = 4
gpa = 1.5
sum = 0
# array determined in section organization
# for now these are testing variables
array = [["Sekhyny, Jywo","GMGldQk","A",4],
         ["Sekhyny, Jywo","GMGldQk","A",4],
         ["Sekhyny, Fyu","GMGldQC","A",4],
         ["Szhmsw, Iuuy","GMMlQdC","A-",4],
         ["Szttzpk, Iheyppy","GMdGudQ","F",4],
         ["Sxzsokx, Oytckn","GMlkdQG","F",4],
         ["Sjxpka, Eytyhek","GMMlRMM","B-",4],
         ["Dcyugkxa, Umxeyp","GMMlCdG","F",4],
         ["Dzppysrctzp, Uemyp","GMMkGMl","A",4],
         ["Rkgyxxza, Newtzxey","GMuuCfG","A-",4],
         ["Qsxtymz, Jzxmyp","GMlMfRC","C",4],
         ["Cyxmep, Dzppzx","GMluClk","A",4],
         ["Cyxmep, Dzppzx","GMluClk","A",4],
         ["Cyxxeazp, Dhyjtzp","GMMfllR","B-",4],
         ["Myxz, Pjhkx","GMfGCQu","A",4],
         ["Mepr, Tehkj","GMfGGGu","A",4],
         ["Oyhhzlle, Jzakic","GMMRufu","W",4],
         ["Aprkxy, Jzacsy","GdkCCkM","NP",4],
         ["Lekxwk, Myukxzp","GMMRllQ","D",4],
         ["Tedkxy, Qxypoek","GMdCGdQ","F",4],
         ["Fwckiuyp, Tjyp","GMdRQdM","A",4],
         ["Pyaakj, Eytcyp","GMMRClQ","B-",4],
         ["Pkwc, Ixew","GMlQMkM","A-",4]
         ]
# array of weighted valuse to find average gpa
gpaArray = []
# array of unweighted GPA values
individualGPA = []
# storage for student info -> resets each iteration of the GPA function
studentInfo = []

# stores student's successes
tempSuccessArray = []
successArray = []

# stores student's failures
tempFailArray = []
failArray = []



# calculates GPA of given section
def GPA(ID, course, s, ch):
    studentInfo = []
    if s == 'A':
        # calculate GPA given credit hours
        gpa = ch * 4.0
        individualGPA.append(4.0)
        studentInfo.append(ID)
        studentInfo.append(course)
        tempSuccessArray.append(studentInfo)

        return gpa
    elif s == 'A-':
        gpa = ch * 3.7
        individualGPA.append(3.7)
        studentInfo.append(ID)
        studentInfo.append(course)
        tempSuccessArray.append(studentInfo)
        return gpa
    elif s == 'B+':
        gpa = ch * 3.3
        individualGPA.append(3.3)
        return gpa
    elif s == 'B':
        gpa = ch * 3.0
        individualGPA.append(3.0)
        return gpa
    elif s == 'B-':
        gpa = ch * 2.7
        individualGPA.append(2.7)
        return gpa
    elif s == 'C+':
        gpa = ch * 2.3
        individualGPA.append(2.3)
        return gpa
    elif s == 'C':
        gpa = ch * 2.0
        individualGPA.append(2.0)
        return gpa
    elif s == 'C-':
        gpa = ch * 1.7
        individualGPA.append(1.7)
        return gpa
    elif s == 'D+':
        gpa = ch * 1.3
        individualGPA.append(1.3)
        # store students' data
        studentInfo.append(ID)
        studentInfo.append(course)
        tempFailArray.append(studentInfo)
        return gpa
    elif s == 'D':
        gpa = ch * 1.0
        individualGPA.append(1.0)
        # store students' data
        studentInfo.append(ID)
        studentInfo.append(course)
        tempFailArray.append(studentInfo)
        return gpa
    elif s == 'D-':
        gpa = ch * 0.7
        individualGPA.append(0.7)
        # store students' data
        studentInfo.append(ID)
        studentInfo.append(course)
        tempFailArray.append(studentInfo)
        return gpa
    elif s == 'F':
        gpa = ch * 0
        individualGPA.append(0)
        # store students' data
        studentInfo.append(ID)
        studentInfo.append(course)
        tempFailArray.append(studentInfo)
        return gpa
    # line allows code to disregard grade letters not mentioned above (ie "I" or "W")
    else:
        gpa = 'NA'
        return gpa


# calculate average GPA
def calcAverageGPA(hours, sumPoints):
    average = sumPoints / hours
    return average


def zScore(average, gpa, n, sum):
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

# calculates gpas of each student given a section array
for row in array:
    # Resets count after each row
    count = 0
    for val in row:
        count += 1
        # if count =1, value is student ID
        if count == 1:
            ID = val
        # if count = 2, value is course ID
        elif count == 2:
            course = val
        # If count = 3, value is the letter grade
        elif count == 3:
            s = val
        # If count = 4, value is credit hours
        elif count == 4:
            # checks if value contains an empty character (represented as a string in this instance
            ch = val
            totalHours += ch
    # calculates gpa of using the given credit hours and grade letter
    gpa = GPA(ID, course, s,ch)

    # sums numerical GPA values
    if (gpa != "NA"):
        sumPoints = gpa + sumPoints
        # add gpa to an array *only float*
        gpaArray.append(gpa)

average = calcAverageGPA(totalHours, sumPoints)

# prints outputs (testing purposes)
print("GPAs of section", gpaArray)
print("Average section gpa", average)

# calculates difference of sums
for val in individualGPA:
    diff = difOfSquares(average, gpa, sum)
    sum = diff

# calculate standard deviation (square root of sum/n-1)
sd = math.sqrt(sum / (len(individualGPA)- 1))

# calculate zscore for each element in gpa Array
for val in individualGPA:
    z = zScore(average, val, len(individualGPA), sum)
    # print element if zscore is significant
    if (z<=-2) or (z>=2):
        print(val, "is significant with a zscore of: ", z)

# removes repeats from tempSuccessArray
for val in tempSuccessArray:
    count = tempSuccessArray.count(val)

    # if student has more than one occurrence
    if count >1:
        for element in successArray:
            if val not in successArray:
                successArray.append(val)
        if not successArray:
            successArray.append(val)

# removes repeats from tempFailArray
for val in tempFailArray:
    count = tempFailArray.count(val)

    # if student has more than one occurrence
    if count >1:
        for element in failArray:
            if val not in failArray:
                failArray.append(val)
        if not failArray:
            failArray.append(val)

# print output of program
print("success: ", successArray)
print('fail: ', failArray)

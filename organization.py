def organization(array):
    A = []
    AMinus = []
    DPlus = []
    D = []
    DMinus = []
    F = []
    for element in array:
        print(element)
        if len(element) > 3:
            if element[0]== 'A':
                A.append(element)
            elif element[0]== 'A-':
                AMinus.append(element)
            elif element[0] == 'D+':
                DPlus.append(element)
            elif element[0] == 'D':
                D.append(element)
            elif element[0] == 'D-':
                DMinus.append(element)
            elif element[0] == 'F':
                F.append(element)


    return A, AMinus, DPlus, D, DMinus, F


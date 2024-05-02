def organization(array):
    A = []
    D = []
    for element in array:
        
        if len(element) > 3:
            if element[0]== 'A' or element[0] == 'A-':
                A.append(element)
            elif element[0] == 'D' or element[0] == 'D+' or element[0] == 'D-' or element[0] == 'F':
                D.append(element)


    return A, D


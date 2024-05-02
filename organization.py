def organization(array):
    A = []
    D = []

    for element in array:
        print(element)
        if len(element) > 3:
            if element[0] == 'A' or element[0] == 'A-':
                A.append(element)
            elif element[0] == 'D' or element[0] == 'D-' or element[0] == 'D+' or element[0] == 'F':
                D.append(element)

    print("A", A)
    print('d', D)
    return A, D


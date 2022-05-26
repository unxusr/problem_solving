def get_duplicated_number():
    elements = {}
    lista = [5, 5, 5, 6, 6, 3, 2, 1,1,8,8, 8, 7]
    for element in lista:
        if lista.count(element) > 1:
            elements[element] = "Repeated " + str(lista.count(element)) + " Times"
    print(elements)


get_duplicated_number()

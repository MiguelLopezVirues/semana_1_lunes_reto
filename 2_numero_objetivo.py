def numero_objetivo(lista, objetivo):
    lista_tuplas = []
    for num in lista:
        lista_sin_num = list(set(lista)-set([num]))
        for other_num in lista_sin_num:
            if num + other_num == objetivo:
                lista_tuplas.append(tuple(sorted([num,other_num])))
    lista_tuplas = list(set(lista_tuplas))
    return lista_tuplas
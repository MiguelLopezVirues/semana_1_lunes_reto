def encontrar_faltante(lista):
    lista_orden = sorted(lista)
    faltante = None
    for i, num in enumerate(lista_orden):
        if num + 1 != lista_orden[i+1]:
            faltante = num + 1
            break

    return faltante

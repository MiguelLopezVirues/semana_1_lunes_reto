# Opcion original
def objetos_mochila(lista, objetivo):
    lista_ord = sorted(lista)
    mochila = []
    for n in range(len(lista_ord)):
        if sum(mochila) + lista_ord[n] <= objetivo:
            mochila.append(lista_ord[n])
    
    return len(mochila)

# Opcion abreviada
def objetos_mochila2(lista, objetivo):
    lista_ord = sorted(lista)
    mochila = [num for i, num in enumerate(lista_ord) if sum(lista_ord[:i+1]) <= objetivo]
    
    return len(mochila)
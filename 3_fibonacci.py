def fibonacci(numero):
    lista_fib = []
    if numero <= 0:
        return lista_fib
    else:
        lista_fib = [0,1]
    
    while (lista_fib[-2]+lista_fib[-1]) <= numero:
        lista_fib.append(lista_fib[-2]+lista_fib[-1])

    
    return lista_fib
def my_reverse(lista):
    retorno=[]
    tam = len(lista)
    for i in range(0, tam):
        retorno.append(lista[tam-1-i])

    return retorno

def reverse_comprehension(lista):
    retorno = [lista[i] for i in range(len(lista)-1,-1,-1)]
    return retorno


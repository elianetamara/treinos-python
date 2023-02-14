def my_slice(sequencia, inicio, fim):
    if type(sequencia) == str:
        retorno = ''
        for i in range(inicio, fim):
            retorno += sequencia[i]
        return retorno
    else:
        retorno = []
        for i in range(inicio, fim):
            retorno.append(lista[i])
        return retorno

def my_slice_jump(lista, inicio, fim, pulo):
    retorno = []
    for i in range(inicio, fim, pulo):
        retorno.append(lista[i])
    return retorno

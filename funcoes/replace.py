def my_replace(seq, novo):
    lista = []
    for i in seq:
        lista.append(i)
    retorno = ''
    for j in range(len(lista)):
        #if condição:
        lista[j] = novo
        retorno += lista[j]
    return lista, retorno

print(my_replace('aeiou', 'b'))

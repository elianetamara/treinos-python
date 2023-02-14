def pop_insert(lista, idx):
    for i in range(idx, 0, -1):
        lista[i], lista[i-1] = lista[i-1], lista[i]

def pop_append(lista, idx):
    for i in range(idx, len(lista)-1):
        lista[i], lista[i+1] = lista[i+1], lista[i]

#######################################################################

def menor(len1, len2):
    if len1 > len2:
        menor = len2
    else:
        menor = len1
    return menor

def ordena_carac(nome1, nome2):
    m = menor(len(nome1), len(nome2))
    for i in range(m):
        if nome1[i] < nome2[i]:
            return nome1
        elif nome1[i] > nome2[i]:
            return nome2

def junta_lista(lista1, elem):
    lista1.append(elem)
    i = len(lista)-2
    while i > 0:
        if ordena_carac(lista1[i], lista[i+1]) == lista[i+1]:
            lista1[i], lista[i+1] = lista[i+1], lista1[i]
        i -= 1

def junta_listas(lista1, lista2):
    for i in lista2:
        junta_lista(lista1, i)

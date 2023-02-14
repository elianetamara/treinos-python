import numpy as np

def eh_igual(lista):
    return np.allclose(lista, lista[0])

def diagonal(M, indice, i):
    diagonal = 0
    for j in M:
        diagonal += j[indice]
        indice += i
    return diagonal

def soma_linha(M, linha):
    soma_linha = 0
    for i in M[linha]:
        soma_linha += i
    return soma_linha

def soma_coluna(M, coluna):
    soma_coluna = 0
    for i in M:
        soma_coluna += i[coluna]
    return soma_coluna

def lista_somas(M):
    lista_somas = []
    lista_somas.append(diagonal(M, 0, 1))
    lista_somas.append(diagonal(M, len(M[0])-1, -1))
    for i in range(len(M)):
        lista_somas.append(soma_linha(M, i))
        lista_somas.append(soma_coluna(M, i))
    return lista_somas

def matriz_magica(M):
    res = lista_somas(M)
    igualdade = eh_igual(res)
    if igualdade:
        return 'S'
    else:
        return 'N'

matriz = [[1,2],[3,4]]
print(matriz_magica(matriz))

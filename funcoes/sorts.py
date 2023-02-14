passos = 0

def bubble_sort(array):
    global passos
    for j in range(len(array)):
        num_trocas = 0
        for i in range(len(array) - 1 - j):
            passos += 1
            if array[i] >= array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
                num_trocas += 1
        if num_trocas == 0:
            return

#selection sort, com base no máximo
passos = 0

def selection_sort(array):
    def i_maior(seq, i_max):
        i_maior = 0
        for i in range(0, i_max + 1):
            if seq[i] > seq[i_maior]:
                i_maior = i
        return i_maior

    for i_d in range(len(array) - 1, -1, -1):
        i_prox = i_maior(array, i_d)
        array[i_d], array[i_prox] = array[i_prox], array[i_d]


passos = 0

def insere_ordenado(array, elemento):
    array.append(elemento)
    bubble_sort(array)


def insere_ordenado(numeros, num):
    numeros.append(num)
    for i in range(len(numeros) - 2, -1, -1):
        if numeros[i + 1] >= numeros[i]: break
        numeros[i + 1], numeros[i] = numeros[i], numeros[i + 1]


numeros = []
while True:
    num = int(input())
    if num < 0: break
    insere_ordenado(numeros, num)

print(numeros)

def bubble_sort(lista):
    for num in range(len(lista)-1, 0, -1):
        for i in range(num):
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux

def insertion_sort(lista):
    for i in range(1, len(lista)):
        aux = lista[i]
        j = i-1
        while j >= 0 and aux < lista[j]:
                lista[j + 1] = lista[j]
                j -= 1
        arr[j + 1] = aux


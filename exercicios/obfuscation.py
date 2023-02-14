def is_space(carac):
    if carac == ' ':
        return True
    return False

def space_ast(codigo, indice):
    palavra = ''
    retorno = ''
    for i in range(len(codigo)):
        if i == indice:
            retorno += len(palavra) * '*'
        if codigo[i].isalpha():
            palavra += codigo[i]
        elif is_space(codigo[i]):
            palavra = ''
    return retorno

def is_carac(carac):
    caracteres = ['a', 'b', 'e', 'g', 'i', 'l', 's', 'o']
    for i in caracteres:
        if carac.lower() == i:
            return True
    return False

def is_num(carac):
    numeros = [4,8, 3, 6, 1, 7, 5, 0]
    for i in numeros:
        if carac.isdigit():
            if int(carac.lower()) == i:
                return True
    return False

def carac_num(carac):
    ret = ''
    caracteres = ['a', 'b', 'e', 'g', 'i', 'l', 's', 'o']
    numeros = [4,8, 3, 6, 1, 7, 5, 0]
    for i in range(len(caracteres)):
        if carac.lower() == caracteres[i]:
            ret += str(numeros[i])
    return ret

def num_carac(carac):
    ret = ''
    caracteres = ['a', 'b', 'e', 'g', 'i', 'l', 's', 'o']
    numeros = [4,8, 3, 6, 1, 7, 5, 0]
    for i in range(len(numeros)):
        if int(carac.lower()) == numeros[i]:
            ret += caracteres[i]
    return ret

def troca(codigo):
    retorno = ''
    for i in codigo:
        if i.islower():
            retorno += i.upper()
        else:
            retorno += i.lower()
    return retorno

def obfusca(codigo):
    codigo = troca(codigo)
    ret = ''
    for i in range(len(codigo)):
        if is_carac(codigo[i]):
            ret += carac_num(codigo[i])
        elif is_num(codigo[i]):
            ret += num_carac(codigo[i])
        elif is_space(codigo[i]):
            ret += space_ast(codigo, i)
        else:
            ret += codigo[i]
    return ret

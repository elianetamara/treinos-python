def my_copy(seq):
    if type(seq) == str:
        retorno = ''
        for i in seq:
            retorno += i
        return retorno
    else:
        retorno = []
        for i in seq:
            retorno.append(i)
        return retorno

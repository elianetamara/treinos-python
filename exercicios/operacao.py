def valida_operador():
    operacoes = ['+', '-', '*', '/']
    while True:
        operacao = input().strip()
        if operacao in operacoes:
            break
        else:
            print('Digite uma operacao válida.')
    return operacao

def calcula(a, b, operacao):
    if operacao == '+':
        resultado = a + b
    elif operacao == '-':
        resultado  = a - b
    elif operacao == '*':
        resultado = a * b
    elif operacao == '/':
        resultado = a/b
    return resultado

def valida_entrada():
    while True:
        try:
            n = float(input())
        except ValueError:
            print('Você digitou algum valor inválido')
        else:
            break
    return n

op = valida_operador()
a = valida_entrada()
b = valida_entrada()

while True:
    try:
        res = calcula(a, b, op)
        print(f'{res:.1f}')
        break
    except EOFError:
        break
    except ZeroDivisionError:
        print("Operação aritmética inválida")
        break
    except ArithmeticError:
        print("Operação aritmética inválida")

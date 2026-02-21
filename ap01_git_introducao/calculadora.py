def somar(*args):
    soma = 0
    for arg in args:
        soma += arg

    return soma

def somarList(lista):
    soma = 0
    for num in lista:
        soma += num

    return soma

def subtrair(a, *args):
    sub = a
    for arg in args:
        sub -= arg

    return sub

def subtrairList(lista):
    sub = lista[0]
    for num in lista[1:]:
        sub -= num

    return sub

def multiplicar(a, b):
    return a*b

def dividir(a, b):
    return a/b

# print(somar(2, 3))
# print(subtrair(2, 3, -2))
# print(multiplicar(7, 8))
# print(dividir(7, 8))
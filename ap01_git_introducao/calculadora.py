def somar(*args):
    soma = 0
    for arg in args:
        soma += arg

    return soma

def subtrair(a, *args):
    sub = a
    for arg in args:
        sub -= arg

    return sub

def multiplicar(a, b):
    return a*b

def dividir(a, b):
    return a/b

print(somar(2, 3))
print(subtrair(2, 3, -2))
print(multiplicar(7, 8))
print(dividir(7, 8))
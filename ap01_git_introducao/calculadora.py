def somar(a, b):
    return a + b

def somar(*args):
    soma = 0
    for arg in args:
        soma += arg

    return soma

print(somar(2, 3))

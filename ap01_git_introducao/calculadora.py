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

print(somar(2, 3))
print(subtrair(2, 3, -2))
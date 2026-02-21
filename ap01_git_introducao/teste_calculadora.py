import calculadora

escolha = 0
opcoes = "1) Somar\n" \
         "2) Subtrair\n" \
         "3) Multiplicar\n" \
         "4) Dividir\n" \
         "-1) Sair"
while (escolha != -1):
    print('Calculadora em Python\nEscolha uma opção:\n' + opcoes)
    escolha = int(input())
    match escolha:
        case 1:
            print("Somar: Digite os números separados por ','")
            numeros = [int(n) for n in input().split(', ')]
            print(f"Resultado: {calculadora.somarList(numeros)}")
            print("")
        case 2:
            print("Subtrair: Digite os números separados por ','")
            numeros = [int(n) for n in input().split(', ')]
            print(f"Resultado: {calculadora.subtrairList(numeros)}")
            print("")
        case 3:
            print("Multiplicar: Digite o primeiro número: ")
            a = int(input())
            print("Digite o segundo número: ")
            b = int(input())
            print(f"Resultado: {calculadora.multiplicar(a, b)}")
            print("")
        case 4:
            print("Dividir: Digite o primeiro número: ")
            a = int(input())
            print("Digite o segundo número: ")
            b = int(input())
            if(b == 0):
                print("Não é possível dividir por 0!\n")
                continue
            print(f"Resultado: {calculadora.dividir(a, b)}")
            print("")
        case default:
            print("Escolha uma opção válida!!!\n")
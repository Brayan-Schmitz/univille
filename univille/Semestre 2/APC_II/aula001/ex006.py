def verifica_numero(num):
    numpar = "par"
    numimpar = "ímpar"

    if num % 2 == 0:
        return numpar
    return numimpar

num = int(input("Digite um número: "))

print(f"Seu número é: {verifica_numero(num)}")
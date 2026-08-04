def numero_fatorial(num):

    resultado = 1

    for i in range(1, num + 1):
        resultado *= i

    return resultado

num = int(input("Digite um número: "))

print(f"{numero_fatorial(num)}")
numeros = {}

while True:
    numero = int(input("Digite um número inteiro: "))

    if numero <= 0:
        break

    if numero in numeros:
        numeros[numero] += 1
    else:
        numeros[numero] = 1

print("\nQuantidade de vezes que cada número foi digitado:")

for numero, quantidade in numeros.items():
    print(numero, ":", quantidade)
'''Estrutura Básica do try e except
Escreva um programa em Python que peça ao usuário para digitar um número inteiro. Use o
bloco try e except para capturar qualquer erro na conversão e exibir a mensagem:
"Entrada inválida! Por favor, digite apenas números." caso a conversão falhe.
'''

try:
    num = int(input("Digite um número: "))

    print(f"Seu número escolhido foi: {num}")

except ValueError:
    print("Entrada inválida! Por favor, digite apenas números.")
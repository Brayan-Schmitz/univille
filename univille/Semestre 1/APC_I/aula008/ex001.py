'''Escreva um programa que peça dois números inteiros e imprima todos os
números inteiros entre eles.'''

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))


if num1 < num2:
    for i in range(num1+1, num2):
        print(i)
else:
    for i in range(num1+1, num2, -1):
        print(i)
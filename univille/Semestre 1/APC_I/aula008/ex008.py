'''Vamos entender a distribuição de idades de pensionistas de uma empresa de
previdência. Escreva um programa que leia as idades de uma quantidade não
informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-
75] e [76-100]. Encerre a entrada de dados com um número negativo.'''

i1 = 0 #[1-25]#
i2 = 0 #[26-50]#
i3 = 0 #[51-75]#
i4 = 0 #[76-100]#

pen = int(input("Digite a idade: "))

while pen != 0:
        if 0 < pen < 25:
            i1 += 1
            pen = int(input("Digite a idade: "))
        elif pen < 50:
            i2 += 1
            pen = int(input("Digite a idade: "))
        elif pen < 75:
            i3 += 1
            pen = int(input("Digite a idade: "))
        elif pen < 100:
            i4 += 1
            pen = int(input("Digite a idade: "))

print(f"A média da idade dos clientes é: \n[1-25] = {i1}\n[26-50] = {i2}\n[51-75] = {i3}\n[76-100] = {i4}")
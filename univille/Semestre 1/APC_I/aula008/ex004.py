'''Desenvolva um programa que leia um conjunto indeterminado de temperaturas
em Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o
valor -273°C.'''

print("Para sair digite a temperatura -273°C")
temp = float(input("Digite a temperatura em Celsius: "))

media = []

while temp != -273:
    media.append(temp)
    temp = float(input("Digite a temperatura em Celsius: "))

print(f"A média das temperaturas em Celsius é: {sum(media)/len(media):.2f}")
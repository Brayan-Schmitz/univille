print("Para sair digite a temperatura -273°C")
temp = float(input("Digite a temperatura em Celsius: "))

media = []

while temp != -273:
    media.append(temp)
    temp = float(input("Digite a temperatura em Celsius: "))

print(f"A média das temperaturas em Celsius é: {sum(media)/len(media):.2f}")
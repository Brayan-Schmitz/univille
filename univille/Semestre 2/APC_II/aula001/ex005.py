def classe_eleitor(idade):
    classe0 = "Não-eleitor"
    classe1 = "Eleitor facultativo"
    classe2 = "Eleitor Obrigatório"

    if  idade < 16:
        return classe0
    elif idade < 18 or idade > 65:
        return classe1
    elif idade >= 18:
        return classe2


idade = int(input("Digite a sua idade: "))

print(f"Você é: {classe_eleitor(idade)}")

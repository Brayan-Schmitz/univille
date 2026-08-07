def classifica_idade(idade):
    if idade >= 60:
        return "Idoso"
    if 18 <= idade <= 59:
        return "Adulto"
    if 12 <= idade <= 17:
        return "Adolescente"
    if idade <= 12:
        return "Criança"


idade = int(input("Digite a sua idade: "))

print(f"Você é: {classifica_idade(idade)}")
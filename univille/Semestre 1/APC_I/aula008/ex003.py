print("As avaliações vão de 0 a 5")
n = int(input("Digite a quantidade de alunos: "))

media = []

for i in range(n):
    nota = float(input("Digite a nota: "))
    media.append(nota)

    while nota < 0 or nota > 5:
        print("As avaliações vão de 0 a 5")
        nota = float(input("Digite a nota: "))
        media.append(nota)

print(f"a média das notas é: {sum(media)/len(media)}")
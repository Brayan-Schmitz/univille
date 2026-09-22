alunos = {}

q = int(input("Digite a quantidade de alunos: "))

for i in range(q):
    nome = input("\nDigite o nome do aluno: ")

    notas = []

    for j in range(4):
        nota = float(input(f"Digite a {j + 1}ª nota: "))
        notas.append(nota)

    alunos[nome] = notas

print("\nResultado:")

for nome, notas in alunos.items():
    menor = min(notas)
    media = (sum(notas) - menor) / 3

    print(f"{nome}:")
    print(f"Notas: {notas[0]:.1f}, {notas[1]:.1f}, {notas[2]:.1f}, {notas[3]:.1f}")
    print(f"Menor nota descartada: {menor:.1f}")
    print(f"Média: {media:.1f}")

    if media >= 6:
        print("Aprovado")
    else:
        print("Reprovado")

    print()
idades = []

idade = int(input("Informe a idade do aluno: "))

while idade >= 0:
    idades.append(idade)
    idade = int(input("Informe a idade do aluno: "))

print(f"As idades digitadas foram: {idades}")
print(f"O aluno mais novo possui: {min(idades)} anos")
print(f"O aluno mais velho possui: {max(idades)} anos")
print(f"A média de idade da sala é: { ((min(idades) + max(idades) ) / 2) :.1f} anos")
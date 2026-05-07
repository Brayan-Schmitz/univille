'''Crie um programa no qual o usuário informe a idade de um número indeterminado de
alunos. Para encerrar a leitura dos dados, o usuário deve informar uma idade negativa.
No final, o programa deve mostrar a média aritmética entre a maior e a menor idade'''

idades = []

idade = int(input("Informe a idade do aluno: "))

while idade >= 0:
    idades.append(idade)
    idade = int(input("Informe a idade do aluno: "))

print(f"As idades digitadas foram: {idades}")
print(f"O aluno mais novo possui: {min(idades)} anos")
print(f"O aluno mais velho possui: {max(idades)} anos")
print(f"A média de idade da sala é: { ((min(idades) + max(idades) ) / 2) :.1f} anos")
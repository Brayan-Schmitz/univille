'''Faça um algoritmo que leia informações de alunos (Matricula, Nota1, Nota2 , Nota3)
com o fim das informações indicado por Matricula = 9999. Para cada aluno deve ser
calculada a média final de acordo com a seguinte fórmula:

 Média final = [(2 * Nota1) +(3* Nota2) +(4* Nota 3)] / 9

Se a média final for igual ou superior a 5, o algoritmo deve mostrar Matrícula, Média
Final e a mensagem "APROVADO".
Se a média final for inferior a 5, o algoritmo deve mostrar Matricula, Média Final e a
mensagem "REPROVADO".
Ao final devem ser mostrados o total de aprovados, o total de alunos da turma e o total
de reprovados.'''

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Média dos alunos")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("caso queira encerrar o programa, digite na Matrícula: 9999")

total_alunos = 0
apv = 0
rep = 0

mtc = int(input("Informe a Matrícula: "))

while mtc != 9999:

    nota1 = float(input("Digite a Nota 1: "))
    nota2 = float(input("Digite a Nota 2: "))
    nota3 = float(input("Digite a Nota 3: "))

    media = ((2 * nota1) + (3 * nota2) + (4 * nota3)) / 9

    print(f"\nMatrícula: {mtc}")
    print(f"Média Final: {media:.2f}")

    if media >= 5:
        print("APROVADO")
        apv += 1
    else:
        print("REPROVADO")
        rep += 1

    total_alunos += 1

    print("-" * 40)

    mtc = int(input("Informe a Matrícula: "))

print("\n=-=-=-=-=-=- RESULTADO FINAL =-=-=-=-=-=-=")
print(f"Total de alunos: {total_alunos}")
print(f"Total de aprovados: {apv}")
print(f"Total de reprovados: {rep}")
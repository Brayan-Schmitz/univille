def aprovacao(aulas, faltas, nota):
    aprovado = 1
    reprovado = 0

    if faltas >= (25/100 * aulas):
        return[reprovado]
    elif nota >= 6:
        return[aprovado]
    
    return[reprovado]

aulas = int(input("Digite o total de aulas da disciplina: "))

faltas = int(input("Digite o total de faltas do aluno: "))

nota = float(input("Digite a nota do aluno: "))

print("--" * 50)
print(f"Caso o aluno tenha o resultado [1] ele será aprovado")
print(f"Caso o aluno tenha o resultado [0] ele será reprovado")
print("--" * 50)
print(f"Conceito do aluno: {aprovacao(aulas, faltas, nota)}")
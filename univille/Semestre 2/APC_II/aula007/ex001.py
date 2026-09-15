turma = {
 "Ana": [7.5, 8.0],
 "Carlos": [5.0, 6.0],
 "Mariana": [9.0, 9.5]
}

print("Estado atual da turma:", turma)

while True:
    aluno = input("Digite o nome do aluno para adicionar uma nova nota (ou 'fim'): ")

    if aluno.lower() == 'fim':
        break

    if aluno in turma:
    nova_nota = float(input(f"Digite a nova nota para {aluno}: "))
    if 0 <= nova_nota <= 10:
        turma[aluno].append(nova_nota)
        print(f"Nota {nova_nota} adicionada com sucesso!")

        else:
            print("Nota inválida! Digite um valor entre 0 e 10.")

    else:
        print("Aluno não encontrado na turma!")

print("--- Médias Atualizadas ---")

for aluno, notas in turma.items():
    media = sum(notas) / len(notas)
    status = "Aprovado" if media >= 7.0 else "Em Recuperação"
    print(f"{aluno}: Média = {media:.2f} [{status}]")

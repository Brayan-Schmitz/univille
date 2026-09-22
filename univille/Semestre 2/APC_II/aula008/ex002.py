alunos = {}

while True:
    matricula = int(input("Digite a matrícula (0 para terminar): "))

    if matricula == 0:
        break

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    curso = input("Digite o curso: ")

    alunos[matricula] = (nome, idade, curso)

print("\nAlunos cadastrados:")
for matricula, dados in alunos.items():
    print("Matrícula:", matricula)
    print("Nome:", dados[0])
    print("Idade:", dados[1])
    print("Curso:", dados[2])
    print()
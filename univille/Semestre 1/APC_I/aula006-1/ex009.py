#9. Faça um Programa para leitura de três notas parciais de um aluno. O
#programa deve calcular a média alcançada por aluno e presentar:
#• A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#• A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#• A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))

media = ((nota1 + nota2 + nota3) / 3)

if nota1 > 10:
    print("Nota 1 é Inválida!!")
    exit()
elif nota2 > 10:
    print("Nota 2 é Inválida!!")
    exit()
elif nota3 > 10:
    print("Nota 3 é Inválida!!")
    exit()
elif media > 10:
    print("Média é Inválida!!")
    exit()

if nota1 < 0:
    print("Nota 1 é Inválida!!")
    exit()
elif nota2 < 0:
    print("Nota 2 é Inválida!!")
    exit()
elif nota3 < 0:
    print("Nota 3 é Inválida!!")
    exit()
elif media < 0:
    print("Média é Inválida!!")
    exit()

if 0 <= media <= 10:
    if media < 7:
        print(f"A média é: {media}")
        print("O aluno está: Reprovado")
    if 7 <= media <= 9:
        print(f"A média é: {media}")
        print(f"O aluno está: Aprovado")
    if media == 10:
        print(f"A média é: {media}")
        print(f"O aluno está: Aprovado com Distinção")
else:
    print("Valor Inválido!")
#5. Faça um programa que lê as duas notas parciais obtidas por um aluno numa
#disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#Média de Aproveitamento
#• Entre 9.0 e 10.0 : A
#• Entre 7.5 e 9.0 : B
#• Entre 6.0 e 7.5 : C
#• Entre 4.0 e 6.0 : D
#• Entre 4.0 e zero : E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
#e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

media = ((nota1 + nota2) / 2)

if media > 10 or nota1 > 10 or nota2 > 10:
    print("Valor Inválido!")
    exit()

if media < 0 or nota1 < 0 or nota2 <0:
    print("Valor Inválido!")
    exit()

print(f"O aluno teve a primeira nota: {nota1}")
print(f"O aluno teve a segunda nota: {nota2}")
print(f"A média do aluno é: {media}")

if 0 <= media <= 10:
    if media <= 4:
        print(f"O conceito do aluno é: E")
        print(f"O aluno foi: REPROVADO")
    elif media <= 6:
        print(f"O conceito do aluno é: D")
        print(f"O aluno foi: REPROVADO")
    elif media <= 7.5:
        print(f"O conceito do aluno é: C")
        print(f"O aluno foi: APROVADO")
    elif media <= 9.0:
        print(f"O conceito do aluno é: B")
        print(f"O aluno foi: APROVADO")
    elif media <= 10.0:
        print(f"O conceito do aluno é: A")
        print(f"O aluno foi: APROVADO")
else:
    print("Valor Inválido!")
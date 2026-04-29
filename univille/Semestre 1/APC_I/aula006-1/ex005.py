#5. Faça um Programa que leia um número e exiba o dia correspondente da
#semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer
#valor inválido

print("Os dias da semana correspodente (1-Domingo, 2- Segunda, etc...) ")
week = input("Digite o dia da semana: ").strip()

if week in ("1", "2", "3", "4", "5", "6", "7"):
    if week in ("1"):
        print("Hoje é Domingo!")
    if week in ("2"):
        print("Hoje é Segunda-feira!")
    if week in ("3"):
        print("Hoje é Terça-feira!")
    if week in ("4"):
        print("Hoje é Quarta-feira!")
    if week in ("5"):
        print("Hoje é Quinta-feira!")
    if week in ("6"):
        print("Hoje é Sexta-feira!")
    if week in ("7"):
        print("Hoje é Sábado!")
else:
    print("Valor Inválido!")
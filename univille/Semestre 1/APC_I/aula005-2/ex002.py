sal = float(input("Qual o seu salário: "))
vem = float(input("Qual o valor do empréstimo: "))
np = int(input("Qual o número de parcelas: "))

limite = sal * (30/100)

valp = vem / np

if valp <= limite:
    print("Seu crédito foi aprovado")
else:
    print("Seu crédito foi negado")
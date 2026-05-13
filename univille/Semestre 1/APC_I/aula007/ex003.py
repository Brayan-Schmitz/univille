'''Com base na tabela salarial da questão anterior, crie um pro grama que informe a
quantidade de médicos com salários superiores a R$ 4.500,00.'''

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Calculadora de média salarial dos médicos")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("caso queira encerrar o programa, digite: 0")

qnts = 0

sal = float(input("Informe o salário: R$ "))

if sal == 0:
    print("Programa encerrado!")
    exit()

while sal != 0:

    if sal > 4500:
        qnts += 1


    sal = float(input("Informe o salário: R$ "))

print(f"A média salarial dos médicos superiores a R$4.500,00, é: {qnts}")
'''Crie um programa no qual o usuário informe o código do cargo de um funcionário (ver
tabela abaixo) e o seu respectivo salário. Para encerrar a leitura dos dados, defina uma
condição de parada (por exemplo, código do cargo igual a zero). Ao fim, o programa deve
informar a média salarial dos nutricionistas'''

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Calculadora de média salarial")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Códigos dos cargos")
print("1 Enfermeiro")
print("2 Nutricionista")
print("3 Médico")
print("caso queira encerrar o programa, digite: 0")

cg = int(input("Informe o código do cargo: "))

if cg == 0:
    print("Programa encerrado!")
    exit()

if cg not in (1, 2, 3):
    print("Código inválido!")
    exit()

sals = []

sal = float(input("Informe o salário: R$ "))

while sal != 0:
    sals.append(sal)
    sal = float(input("Informe o salário: R$ "))

print(f"A média salarial do cargo é: R$ { sum(sals) / len(sals) :.2f}")

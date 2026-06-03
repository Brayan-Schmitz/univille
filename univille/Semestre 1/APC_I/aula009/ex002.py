'''Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima
de 3000 reais e calcule a porcentagem quanto ao total de compras.'''

gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

acima_3000 = 0
qnt_3000 = 0

for i in gastos:
    if i > 3000:
        acima_3000 += i
        qnt_3000 += 1

porcentagem = acima_3000 * 100 / sum(gastos)

print(f"Compras acima de R$3.000,00: {qnt_3000}")
print(f"Porcentagem: {porcentagem:.2f}%")

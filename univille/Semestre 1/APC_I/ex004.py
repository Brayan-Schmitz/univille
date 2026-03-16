sal = float(input("Digite o salário atual: "))
sal_amt = float(input("Digite a porcentagem de aumento: "))
amt = sal * (sal_amt / 100)
nv_sal = sal + amt
print("Um aumento de {:.2f} em um salário de R${:.2f}".format(sal_amt, sal))
print("é igual a um aumento de R${:.2f}".format(amt))
print("Resultando em um novo salário de R${:.2f}".format(nv_sal))

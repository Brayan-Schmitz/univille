valhrs = float(input("Qual o valor da sua hora trabalhada: R$"))
numhrs = int(input("Quantas horas você trabalha no mês: "))
inss = float(input("Qual é o desconto do INSS: "))

salbr = valhrs * numhrs
salliq = salbr * ((inss)/100)

print("Seu salário líquido é R${}".format(salliq))
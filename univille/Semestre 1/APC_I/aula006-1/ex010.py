#10. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#• Até 5 Kg:
#File Duplo R$ 24,90 por Kg
#Alcatra R$ 25,90 por Kg
#Picanha R$ 46,90 por Kg
#• Acima de 5 Kg:
#File Duplo R$ 25,80 por Kg
#Alcatra R$ 26,80 por Kg
#Picanha R$ 37,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos
#de carne da promoção, porém não há limites para a quantidade de carne por
#cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
#desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo
#e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
#contendo as informações da compra: tipo e quantidade de carne, preço total,
#tipo de pagamento, valor do desconto e valor a pagar

pprint("As opções de corte da carne são: FD: Filé Duplo")
print("As opções de corte da carne são: AL: Alcatra")
print("As opções de corte da carne são: PI: Picanha")

tipo = input("Digite o tipo da carne: ").strip().upper()

if tipo not in ("FD", "AL", "PI"):
    print("Tipo de carne inválido")
    exit()

qnt = float(input("Digite a quantidade de carne (Kg): "))

if qnt <= 0:
    print("Quantidade inválida!")
    exit()

pgt = input("Pagamento com cartão Tabajara? (S/N): ").strip().upper()
if pgt not in ("S", "N"):
    print("Tipo de pagamento inválido!")
    exit()

if tipo == "FD":
    preco_kg = 24.90 if qnt <= 5 else 25.80
    nome_carne = "Filé Duplo"
elif tipo == "AL":
    preco_kg = 25.90 if qnt <= 5 else 26.80
    nome_carne = "Alcatra"
else:  
    preco_kg = 46.90 if qnt <= 5 else 37.80
    nome_carne = "Picanha"


total = qnt * preco_kg
desconto = total * 0.05 if pgt == "S" else 0
valor_a_pagar = total - desconto

print(f"Carne: {nome_carne}")
print(f"Quantidade: {qnt:.2f} Kg")
print(f"Preço por Kg: R$ {preco_kg:.2f}")
print(f"Total: R$ {total:.2f}")
print(f"Pagamento com cartão Tabajara: {'Sim' if pgt=='S' else 'Não'}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")

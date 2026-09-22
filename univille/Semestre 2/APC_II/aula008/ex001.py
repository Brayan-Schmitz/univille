estoque = {}

while True:
    codigo = int(input("Digite o código da peça (0 para terminar): "))

    if codigo == 0:
        break

    quantidade = int(input("Digite a quantidade: "))

    if codigo in estoque:
        print("Esse código já está cadastrado. Dados descartados.")
    else:
        estoque[codigo] = quantidade

print("\nDados do estoque:")
for codigo, quantidade in estoque.items():
    print(codigo, ":", quantidade)
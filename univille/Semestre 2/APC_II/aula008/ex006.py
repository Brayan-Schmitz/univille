contatos = {}

while True:
    nome = input("Digite o nome (Enter para terminar): ")

    if nome == "":
        break

    idade = int(input("Digite a idade: "))
    telefone = input("Digite o telefone: ")

    contatos[nome] = (idade, telefone)

print("\nContatos em ordem alfabética:")

for nome in sorted(contatos):
    idade, telefone = contatos[nome]

    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Telefone: {telefone}")
    print()

# Criando os dois novos dicionários
menores = {}
maiores = {}

for nome, dados in contatos.items():
    idade = dados[0]
    telefone = dados[1]

    if idade < 18:
        menores[nome] = (idade, telefone)
    else:
        maiores[nome] = (idade, telefone)

# Eliminando o dicionário original
del contatos

print("Menores de 18 anos:")
print(menores)

print("\nMaiores ou iguais a 18 anos:")
print(maiores)
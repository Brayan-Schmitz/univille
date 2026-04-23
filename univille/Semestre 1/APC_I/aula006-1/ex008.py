#8. Faça um Programa que leia um número inteiro menor que 1000 e imprima a
#quantidade de centenas, dezenas e unidades do mesmo. Observando os termos
#no plural a colocação do "e", da vírgula entre outros. Exemplo:
#• 326 = 3 centenas, 2 dezenas e 6 unidades
#• 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301,
#101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

print("Digite um número inteiro menor que 1000")
num = int(input("Digite o número inteiro: "))

num = str

if len(num) >= 4:
    print("Número Inválido!")
    exit()

if len(num) == 3:
    print(f"Seu número {num} \nPossui {num[0]} centenas, {num[1]} dezenas e {num[2]} unidades.")
elif len(num) == 2:
    print(f"Seu número {num} \nPossui {num[0]} dezenas e {num[1]} unidades.")
elif len(num) == 1:
    print(f"Seu número {num} \nPossui {num[0]} unidades.")
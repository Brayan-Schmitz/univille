'''Os números primos possuem várias aplicações dentro da Ciência de Dados em
criptografia e segurança, por exemplo. Um número primo é aquele que é divisível
apenas por um e por ele mesmo. Assim, faça um programa que peça um número
inteiro e determine se ele é ou não um número primo.'''

num = int(input("Digite um número: "))
if num / 1 == num and num / num == num:
    print("O número é primo.")
else:
    print("O número não é primo.")
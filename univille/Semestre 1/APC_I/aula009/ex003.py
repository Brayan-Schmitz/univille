'''Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista.
Exemplo: [1,4,7,2,4].'''

nums = []

for i in range(5):
    num = int(input("Digite um número: "))
    nums.append(num)

print(nums)
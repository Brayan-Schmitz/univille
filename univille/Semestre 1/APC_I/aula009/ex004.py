'''Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.'''

nums = []

for i in range(5, 1, -1):
    num = int(input("Digite um número: "))
    nums.append(num)

print(nums[::-1])
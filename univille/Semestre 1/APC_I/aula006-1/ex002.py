#2. Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

nums = [num1, num2, num3]

ord = sorted(nums, reverse= True)

print(f"Os números em ordem decrescentes é {ord}")
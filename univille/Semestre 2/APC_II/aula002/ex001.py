def eh_par(num):
    numpar = True
    numimpar = False

    if num % 2 == 0:
        return numpar
    return numimpar

num = int(input("Digite um número: "))

print("--" * 50)
print(f"Caso o resultado seja True o número é par")
print(f"Caso o resultado seja False o número é ímpar")
print("--" * 50)

print(f"{eh_par(num)}")
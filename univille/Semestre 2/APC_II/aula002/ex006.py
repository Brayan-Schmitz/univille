soma = []

def soma_ate_n(n):
    for i in range(0, n +1, 1):
        soma.append(i)
    return sum(soma)

n = int(input("Digite um número: "))

print(f"A soma total de números até N é: {soma_ate_n(n)}")
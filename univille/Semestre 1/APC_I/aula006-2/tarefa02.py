import random

numero_secreto = random.randint(1, 10)

tentativas = []

for i in range(1, 4):
    tentativa = int(input(f"Jogador {i}, digite sua tentativa (1-10): "))
    tentativas.append(tentativa)

ganhadores = []
for i, tentativa in enumerate(tentativas, start=1):
    if tentativa == numero_secreto:
        ganhadores.append(f"Jogador {i}")

print("\nNúmero sorteado:", numero_secreto)

if ganhadores:
    print("Parabéns! Acertou:", ", ".join(ganhadores))
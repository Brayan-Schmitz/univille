print("Digite 1000 para encerrar")

notas = []

while True:
    nota = float(input("Digite sua nota: "))

    if nota == 1000:
        break

    notas.append(nota)

print("Notas digitadas:", notas)
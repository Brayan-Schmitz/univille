name = input("Digite o nome do candidato: ")
notap = float(input("Digite a nota de Português: "))
notam = float(input("Digite a nota de Matemática: "))
notacg = float(input("Digite a nota de Conhecimentos Gerais: "))

media = (notap + notam + notacg) / 3

print("O candidato, {}, tem as notas: \nNota de Português {} \nNota de Matemática {} \nNota de Conhecimentos Gerais {}". format(name, notap, notam, notacg))
print("A média do candidato, {}, é {}".format(name, media))

if (media >= 7 and notap > 5 and notam > 5 and notacg > 5):
    print(f"O candidato, {name}, foi aprovado")
else:
    print(f"O candidato, {name}, não foi aprovado")
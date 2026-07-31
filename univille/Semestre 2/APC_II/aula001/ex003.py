def conceito_nota(nota):

    conceito = ["A", "B", "C", "D", "F"]

    if 9 <= nota <= 10:
        return conceito[0]
    
    elif 8 <= nota <= 9:
        return conceito[1]

    elif 7 <= nota <= 8:
        return conceito[2]
    
    elif 6 <= nota <= 7:
        return conceito[3]

    elif nota < 6:
        return conceito[4]

nota = int(input("Digite o valor da Nota: "))

print(f"O conceito da nota é: {conceito_nota(nota)}")
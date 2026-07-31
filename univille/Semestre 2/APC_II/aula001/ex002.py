def valor_perimetro(ladoa, ladob, ladoc):

    perimetro = (ladoa + ladob + ladoc)

    return perimetro

ladoa = int(input("Digite o valor do Lado A: "))

ladob = int(input("Digite o valor do Lado B: "))

ladoc = int(input("Digite o valor do Lado C: "))

print(f"O valor do perimetro é: {valor_perimetro(ladoa, ladob, ladoc)}")

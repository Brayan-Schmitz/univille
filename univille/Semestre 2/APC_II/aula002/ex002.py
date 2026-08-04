def maior_de_dois(numa, numb):
    if numa == numb:
        return numa and numb
    if numa > numb:
        return numa
    if numa < numb:
        return numb

numa = int(input("Digite o número A: "))

numb = int(input("Digite o número B: "))

print(f"O maior número é: {maior_de_dois(numa, numb)}")
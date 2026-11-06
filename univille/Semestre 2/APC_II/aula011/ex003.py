#insertion sort
lista = [7,1,1,6,2]

for i in range(1,len(lista)):
    menor = lista[i]
    j = i - 1
    while j >= 0 and lista[j] > menor:
        lista[j + 1] = lista[j]
        j -= 1
    lista[j + 1] = menor

print(lista)
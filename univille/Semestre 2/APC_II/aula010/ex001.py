aux = [4,8,9]

temp  = []

for i in aux:
    temp.append(i)

for i in range(len(aux)):
    aux[i] = aux[i] + 10

print(temp)
print(aux)
#insertion sort
l = [7,2,1,3,8]

for i in range(1, len(l)):
    menor = l[i]
    j = i - 1

    while j >= 0 and menor < l[j]:
        j = j - 1
        
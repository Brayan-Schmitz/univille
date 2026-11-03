l = [7,5,3,2,1]

for i, valor in enumerate(l):
    for c, d in enumerate(l):
        if (i < c):
            l[i], l[c] = l[c], l[i]
            
print(l)
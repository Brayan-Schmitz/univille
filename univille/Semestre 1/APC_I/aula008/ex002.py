'''Escreva um programa para calcular quantos dias levará para a colônia de uma
bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas
de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia
com 4 elementos e a B com 10.'''

bacA = 4
bacB = 10
dias = 0

while bacA <= bacB:
    bacA = bacA + bacA*3/100
    bacB = bacB + bacB*1.5/1500
    dias += 1

print(f"Total de dias {dias}")
print(f"Bactéria A {bacA}")
print(f"Bactéria B {bacB}")
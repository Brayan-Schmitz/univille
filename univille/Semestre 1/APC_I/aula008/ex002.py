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
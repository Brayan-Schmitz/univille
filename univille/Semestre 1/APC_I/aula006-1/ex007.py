#7. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
#informar se os valores podem ser um triângulo. Indique, caso os lados formem
#um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. Dicas:
#• Três lados formam um triângulo quando a soma de quaisquer dois lados
#for maior que o terceiro;
#• Triângulo Equilátero: três lados iguais;
#• Triângulo Isósceles: quaisquer dois lados iguais;
#• Triângulo Escaleno: três lados diferentes;

a = float(input("Digite o primeiro lado do triângulo: "))
b = float(input("Digite o segundo lado do triângulo: "))
c = float(input("Digite o terceiro lado do triângulo: "))

if a + b > c and a + c > b and b + c > a:
    print("Os lados formam um triângulo")
else:
    print("Os lados não formam um triângulo!")
    exit()

if a == b == c:
    print("O triângulo é um triângulo Equilátero")
elif a == b or b == c or c == a:
    print("O triângulo é um triângulo Isósceles")
else:
    print("o triângulo é um triângulo Escaleno")
'''Captura de Exceções Específicas
Crie uma calculadora simplificada de divisão que solicite dois valores ao usuário e exiba o
resultado da divisão do primeiro pelo segundo. Trate especificamente os seguintes erros com
mensagens personalizadas:
ValueError: Caso o usuário digite algo que não possa ser convertido para número
(float ou int).
ZeroDivisionError: Caso o usuário tente dividir por zero.'''

try:
    num1 = int(input("Digite um número inteiro: "))

    num2 = int(input("Digite um novo número: "))

    div = num1 / num2

    print(f"O resultado da sua divisão é: {div}")

except ValueError:
    print("Entrada inválida! Esse valor não pode ser dividido")

except ZeroDivisionError:
    print("Entrada inválida! Não pode dividir por 0")
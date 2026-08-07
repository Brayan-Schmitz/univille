def calculadora(num1, num2, operacao):
    if operacao == "+":
        return num1 + num2
    if operacao == "-":
        return num1 - num2
    if operacao == "*":
        return num1 * num1
    if operacao == "/":
        if num2 == 0:
            return "Operação inválida! o número não pode ser divisivel por 0"
        return num1 / num2

num1 = int(input("Digite um número: "))

num2 = int(input("Digite um novo número: "))

print("Operações aceitas: +; -; *; /")
operacao = str(input("Digite uma operação: "))

print(f"O resultado da operação é: {calculadora(num1, num2, operacao)}")
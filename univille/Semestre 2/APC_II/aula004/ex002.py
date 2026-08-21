def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1

    return fibonacci(num - 1) + fibonacci(num - 2)


num = int(input("Digite o termo da sequência de Fibonacci:  "))

print(fibonacci(num))
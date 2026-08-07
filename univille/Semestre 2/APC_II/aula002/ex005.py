import time

def contagem_regressiva(inicio):
    for inicio in range(inicio, 0, -1):
        print(inicio)
        time.sleep(1)

inicio = int(input("Digite o tempo: "))

print(f"{contagem_regressiva(inicio)}")
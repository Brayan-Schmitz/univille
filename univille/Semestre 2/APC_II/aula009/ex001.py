'''Exercício 10.1
Escreva uma função chamada nested_sum que receba uma lista de listas de números inteiros e adicione os elementos de todas as listas aninhadas. Por exemplo:

>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def nested_sum(t):
    total = 0
    for lista in t:
        for numero in lista:
            total += numero
    return total


t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


'''Exercício 10.2
Escreva uma função chamada cumsum que receba uma lista de números e retorne a soma cumulativa; isto é, uma nova lista onde o i-ésimo elemento é a soma dos primeiros i+1 elementos da lista original. Por exemplo:

>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def cumsum(t):
    resultado = []
    total = 0

    for numero in t:
        total += numero
        resultado.append(total)

    return resultado


t = [1, 2, 3]
print(cumsum(t))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Exercício 10.3
Escreva uma função chamada middle que receba uma lista e retorne uma nova lista com todos os elementos originais, exceto os primeiros e os últimos elementos. Por exemplo:

>>> t = [1, 2, 3, 4]
>>> middle(t)
[2, 3]'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def middle(t):
    return t[1:-1]


t = [1, 2, 3, 4]
print(middle(t))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

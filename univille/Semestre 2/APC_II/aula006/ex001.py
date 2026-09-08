'''Validação Contínua de Entrada de Dados

Crie uma função chamada solicitar_idade() que peça ao usuário para digitar sua idade no
console. O programa deve garantir que a entrada seja totalmente válida antes de continuar a
execução. Atenda aos seguintes requisitos:


Repetição: Utilize um loop while que continue solicitando a idade até que uma entrada correta
seja fornecida.


Conversão: Tente converter o valor digitado para um número inteiro. Se o usuário digitar um
texto ou caractere inválido (ex: "vinte"), capture o ValueError e exiba a mensagem:
"Entrada inválida! Digite apenas números inteiros.".


Validação com raise: Se a conversão for bem-sucedida, verifique se o número está entre 0 e
120. Caso esteja fora dessa faixa, lance manualmente uma exceção utilizando:
raise ValueError("Idade fora do intervalo permitido (0 a 120 anos).")


Captura da Regra: Capture também a mensagem do raise para orientar o usuário.


Retorno: Retorne o valor numérico da idade assim que for validado com sucesso.'''

def solicitar_idade():
    while True:
        entrada = input("Digite sua idade: ")

        try:
            idade = int(entrada)

            if idade < 0 or idade > 120:
                raise ValueError("Idade fora do intervalo permitido (0 a 120 anos).")

            return idade

        except ValueError as erro:
            if str(erro) == "Idade fora do intervalo permitido (0 a 120 anos).":
                print(erro)
            else:
                print("Entrada inválida! Digite apenas números inteiros.")


idade = solicitar_idade()
print(f"Idade válida: {idade}")

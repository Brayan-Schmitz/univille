def eh_palidromo(palavra):
    if(len(palavra) <= 1):
        print("Palindromo")
        return

    primeira = palavra[0]
    ultima = palavra[-1]

    if(primeira != ultima):
        print("Não palindromo")
        return
    palavra = palavra[1:-1]

    eh_palidromo(palavra)


palavra = input("Insira uma palavra: ")
eh_palidromo(palavra.strip().lower())
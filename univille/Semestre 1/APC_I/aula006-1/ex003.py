#3. Faça um Programa que pergunte em que turno você estuda. Peça para digitar
#M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!",
#"Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print("Os turnos dispóniveis são: M-matutino ou V-Vespertino ou N- Noturno.")
turno = input("Que turno você estuda: ").strip().upper()

if turno in ("m", "v", "n"):
    if turno in ("m"):
        print("Bom dia!")
    if turno in ("v"):
        print("Boa tarde!")
    if turno in ("n"):
        print("Boa noite!")
else:
    print("Valor Inválido!")
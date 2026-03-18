distance = float(input("Digite a distâcia em km: "))
speed = float(input("Digite a velocidade média em m/h: "))
temp = (distance/speed)
#parte inteira
temp_sec = int(temp * 3600)
#convertemos de horas para segundos
hrs = int(temp_sec / 3600)
minute = int(temp_sec / 60)
#o resto
temp_s = int(temp_sec % 3600)
sec = int(temp_s % 60)
#Opcional: imprimir o tempo em horas, minutos, segundos
print("O tempo estimado é de {} horas".format(temp))
print("{} {} {} (horas, minutos, segundos)".format(hrs, minute, sec))

#Programa que leia segundos e converta o tempo em dias, horas e minutos.
import math
segundos = int(input('Informe uma quantidade de segundos: '))
if segundos < 60:
    print(f'O tempo de {segundos} segundos não é o suficiente para contado como inteiro em medidas maiores de tempo.')
elif segundos < 3600:
    print(f'O tempo de {segundos} segundos é equivalente a {math.floor(segundos/60)} minutos e {segundos%60} segundos.')
elif segundos < 3600*24:
    print(f'O tempo de {segundos} segundos é equivalente a {math.floor(segundos/3600)} horas e {math.floor((segundos%3600)/60)} minutos e {(segundos%1440)%60} segundos.')
else:
    print(f'O tempo de {segundos} segundos é equivalente a {math.floor(segundos/(3600*24))} dias, {math.floor(segundos%3600)} horas, {math.floor(segundos%3600/60)} minutos e {math.floor((segundos%3600)%60)} segundos.')
    

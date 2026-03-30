print('-='*10,'PROGRAMA CONVERSÃO TEMPERATURA','-='*10)
#ENTRADA
fah = float(input('Informe a temperatura fahrenheit:'))
#PROCESSAMENTO
c = 5 * ((fah - 32) / 9)
print(f'{fah} Fahrenheit convertido para Celsius {c:.2f}º')
print('FIM DO PROGRAMA')


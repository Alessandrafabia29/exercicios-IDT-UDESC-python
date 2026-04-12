print('-='*10,'PROGRAMA FRUTARIA','-='*10)
#entradas preço de cada fruta
quantMorango = float(input('Informe a quantidade da fruta morango (Kg): '))
quantMacas = float(input('Informe a quantidade da fruta maça (Kg): '))
#CALCULO DO PREÇO DO MORANGO
if quantMorango <=5: #quantidade de kg
    valorMorango = 2.50 * quantMorango
else:
    valorMorango = 2.20 * quantMorango
#CALCULO DO PREÇO DA MAÇA
if quantMacas <= 5:
    valorMaca = 1.80 * quantMacas
else:
    valorMaca = 1.50 * quantMacas
#calculo total sem desconto
totalKilos = quantMorango + quantMacas
totalValor = valorMorango + valorMaca
#verificação do desconto
if totalKilos > 10 or totalValor > 20:
    desconto = totalValor * (5/100)
    totalValor = totalValor - desconto

#Saída
print('RESUMO DA COMPRA:')
print(f'Total de frutas: {totalKilos:.2f}kg')
print(f'Tota a pagar: R$ {totalValor:.2f}')
print('-='*10,'FIM DO PROGRAMA','-='*10)
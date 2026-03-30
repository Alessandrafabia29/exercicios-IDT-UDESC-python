print('-='*10,'PROGRAMA FRUTARIA','-='*10)
quantMorango = int(input('Informe a quantidade da fruta morango: '))
quantMacas = int(input('Informe a quantidade da fruta maça: '))
if quantMorango and quantMacas <=5: #quantidade de kg
    valorMorango = 2.50 * quantMorango
    valorMaca = 1.80 * quantMacas
else:
    valorMorango = 2.20 * quantMorango
    valorMaca = 1.50 * quantMacas
#calcular desconto 5%
if valorMorango or valorMaca > 20:
    pagar = valorMorango * (5/100)
    pagar = valorMaca * (5/100)
elif quantMacas or quantMorango > 10:
    pagar = valorMaca * (5/100)
    pagar = valorMorango * (5/100)
    totalPagar = pagar - valorMaca
    totalPagar = pagar - valorMorango
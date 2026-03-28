print('-='*10,'PROGRAMA CÁLCULO PESCADOS','-='*10)
#entrada
peso = float(input('Informe o peso do pescado: Kg'))
limite = 50
#processamento
excesso = max(0,peso - limite)
multa = excesso * 4
#saída
print(f'Seu excesso foi de {excesso:.2f} kg')
print(f'O valor da multa R$ {multa:.2f}')
print('FIM DO PROGRAMA')


print('-='*10,'PROGRAMA DISTÂNCIA ENTRE DOIS PONTOS','-='*10)
#ENTRADA
x1 = float(input('Informe um valor para o plano x1: '))
y1 = float(input('Informe um valor para o plano y1: '))
x2 = float(input('Informe um valor para o plano x2: '))
y2 = float(input('Informe um valor para o plano y2: '))
#processamento
#cálculo da distância
d = ((x2-x1)**2 + (y2-y1)**2)**0.5
#saída
print(f'A distância entre os pontos: {d:.2f}')
print('-='*10,'FIM DO PROGRAMA','-='*10)
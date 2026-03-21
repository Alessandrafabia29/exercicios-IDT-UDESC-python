print('-='*10,'\033[35mPROGRAMA DISTÂNCIA ENTRE PONTOS\033[m','-='*10)
#Entrada de Dados
x1 = float(input('Informe a distância para x1: '))
x2 = float(input('Informe a distância para x2: '))
y1 = float(input('Informe a distância para y1: '))
y2 = float(input('Informe a distância para y2: '))
#Processamento
#Cálculo da distância
d = ((x2-x1)**2 + (y2-y1)**2)**0.5
#Saída
print(f'A distância entre os pontos {d:.2f}')
print('-='*10,'\033[31mFIM DO PROGRAMA\033[m','-='*10)



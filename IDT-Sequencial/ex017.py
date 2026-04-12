print('-='*10,'PROGRAMA LOJA DE TINTAS','-='*10)
#entrada de dados
area = float(input('Informe o tamanho da área em m2 :'))
#cálculos de 10% de folga
litrosNecessarios = (area * 1.1) / 6 #1 litro cobre 6 m2 + 10% de folga
#situação apenas latas 18 litros
latas = int((litrosNecessarios /18) + 0.999) #para arredondar somamos 0.999 e pegamos a parte inteira
preçoLata = latas * 80
#situação apenas galão 3,6 litros
galao = int((litrosNecessarios/3.6) + 0.999)
preçoGalao = galao * 25
#misturar latas e galões
#pegamos a parte inteira de latas
misturaLatas = int(litrosNecessarios/18)
#calculamos quanto tinta sobrou q as latas não cobriram
restoTinta = litrosNecessarios - (misturaLatas * 18)
#o que sobrou dividimos pelo galão e arredondamos para cima
misturaGalao = int((restoTinta / 3.6)+ 0.999)
#cálculo do preço final da mistura
preçoMistura = (misturaLatas * 80) + (misturaGalao * 25)
#saída de dados
print(f'1-Apenas latas de (18l) : {latas} - Total Valor : R$ {preçoLata:.2f}')
print(f'2-Apenas Galões de (3,6l) : {galao} - Total Valor : R$ {preçoGalao:.2f}')
print(f'3-Mistura: {misturaLatas} latas e {misturaGalao} galões - Total Valor : R$ {preçoMistura:.2f}')
print('-='*10,'FIM DO PROGRAMA','-='*10)

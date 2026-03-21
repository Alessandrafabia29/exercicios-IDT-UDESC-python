print('-='*10,'\033[34mPROGRAMA CONVERSÃO\033[m','-='*10)
valor = float(input('Informe o valor em metros: '))
centimetros = valor * 100
print(f'{valor} metros transformados em centímetros {centimetros:.2f}')
print('-='*10,'\033[34mPROGRAMA CÁLCULO DE ÁREA\033[m','-='*10)
raio = float(input('Informe o valor do raio: '))
area = 3.14*raio**2
print(f'A área do círculo {area:.2f}')
lado = float(input('Informe o valor do lado do quadrado: '))
areaQuadrado = lado ** 2
dobroArea = 2 * areaQuadrado
print(f'O dobro da área do quadrado {dobroArea}')

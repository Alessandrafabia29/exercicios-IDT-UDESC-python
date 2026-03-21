print('-='*10,'\033[36mPROGRAMA EQUAÇÃO DO 2ºGRAU\033[m','-='*10)
#Entrada de dados
a = float(input('Informe o valor de a para equação do 2ºgrau:'))
b = float(input('Informe o valor de b para a equação do 2ºgrau:'))
c = float(input('Informe o valor de c para a equaçãodo 2ºgrau:'))

#processamento
calculoDelta = b**2-4*a*c   #calculo delta
x1 = (-b+calculoDelta**0.5)/(2*a)  #calculo das raízes reais
x2 = (-b-calculoDelta**0.5)/(2*a)  #calculo das raízes reais


#saídas
print(f'O valor de delta para a equação  {calculoDelta}')
print(f'O valor das raízes reais x1{x1:.2f} e x2{x2:.2f}.')
print('-='*10,'\033[35mFIM DO PROGRAMA\033[m','-='*10)

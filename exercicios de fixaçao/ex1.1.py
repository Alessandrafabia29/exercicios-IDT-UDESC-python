print('-='*10,'PROGRAMA EQUAÇÃO DO SEGUNDO GRAU','-='*10)
#ENTRADA
a = float(input('Informe um valor para a: '))
b = float(input('Informe um valor para b: '))
c = float(input('Informe um valor para c: ')) 
#processamento
if a == 0:
    print('O valor de a não pode ser zero em uma equação de 2º grau.')
#cálculo de delta
else:
    delta = b**2 - 4*a*c
    print(f'Delta: {delta:.2f}')
#cálculo das raízes
    if delta < 0:
        print('A equação não possui raízes reais(delta negativo)')
    else:
        x1 = (-b + delta**0.5)/(2*a)
        x2 = (-b - delta**0.5)/(2*a)
#saída raizes da equação de segundo grau
        print(f'raíz 1 : {x1:.2f}')
        print(f'raíz 2 : {x2:.2f}')
print('-='*10,'FIM DO PROGRAMA','-='*10)

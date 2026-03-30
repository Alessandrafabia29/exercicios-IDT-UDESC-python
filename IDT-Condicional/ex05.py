print('-='*10,'PROGRAMA VERIFICAÇÃO TRIÂNGULO','-='*10)
#ENTRADA
l1 = float(input('Informe o primeiro lado: '))
l2 = float(input('Informe o segundo lado: '))
l3 = float(input('Informe o terceiro lado:'))
#PROCESSAMENTO #saída
if (l1+l2)>l3 and (l1+l3)>l2 and (l2+l3)>l1:
    print('Os lados informados podem formar um triângulo.')
    if l1 == l2 == l3:
        print('TRIÂNGULO EQUILÁTERO')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('TRIÂNGULO ISÓSCELES')
    elif l1 != l2 != l3:
        print('TRIÂNGULO ESCALENO')
else:
    print('Os lados informados não podem formar um triângulo.')
print('-='*10,'FIM DO PROGRAMA','-='*10)

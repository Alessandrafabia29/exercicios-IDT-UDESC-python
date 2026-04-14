print('-='*10,'PROGRAMA NÚMEROS DECRESCENTES','-='*10)
n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
n3 = int(input('Informe o terceiro valor: '))
if n1 > n2 and n1 > n2:
    if n2 > n3:
        primeiro,segundo,terceiro = n1,n2,n3
    else:
        primeiro,segundo,terceiro = n1,n3,n2
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        primeiro,segundo,terceiro = n2,n1,n3
    else:
        primeiro,segundo,terceiro = n2,n3,n1
else:
    if n1 > n2:
        primeiro,segundo,terceiro = n3,n1,n2
    else:
        primeiro,segundo,terceiro = n3,n2,n1
#saída
print(f'Os valores em ordem decrescente são: {primeiro} , {segundo} ,{terceiro}')
print('-='*10,'FIM DO PROGRAMA','-='*10)

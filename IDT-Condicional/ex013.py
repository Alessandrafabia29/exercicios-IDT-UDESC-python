print('-='*10,'PROGRAMA MAIOR NÚMERO','-='*10)
n1 = float(input('Informe o primeiro número:'))
n2 = float(input('Informe o segundo número:'))
n3 = float(input('Informe o terceiro número:'))
#verificar qual é o maior
if n1 >= n2 and n1 >= n3:
    maior = n1
    print(f'O número maior entre {n1,n2,n3} é : {maior}')
elif n2 >= n1 and n2 >= n3:
    maior = n2
    print(f'O número maior entre {n1,n2,n3} é : {maior}')
else:
    maior = n3
#saida
if n1 == n2 == n3:
    print('Os três números informados são iguais.')
elif (n1 == n2 == maior) or (n1 == n3 == maior) or (n2 == n3 == maior):
    print(f'Dois números são maiores e iguais: {maior}')
else:
    print(f'O maior número entre {n1} , {n2} , {n3} é {maior}.')
print('-='*10,'FIM DO PROGRAMA','-='*10)
                                                    
    
 





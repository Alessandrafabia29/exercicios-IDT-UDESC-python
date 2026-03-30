print('-='*10,'CÁLCULO ANO BISSEXTO','-='*10)
ano = int(input('Informe o ano:'))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} não é bissexto.')
print('-='*10,'FIM DO PROGRAMA','-='*10)

print('-='*10,'PROGRAMA CALENDÁRIO SEMANAL','-='*10)
num = int(input('Informe um número para ver seu dia da semana correspondente:'))
if num == 1:
    print('DOMINGO')
elif num == 2:
    print('SEGUNDA-FEIRA')
elif num == 3:
    print('TERÇA-FEIRA')
elif num == 4:
    print('QUARTA-FEIRA')
elif num == 5:
    print('QUINTA-FEIRA')
elif num == 6:
    print('SEXTA-FEIRA')
elif num == 7:
    print('SÁBADO')
else:
    print('\033[31mValor inválido.Sem correspondência.\033[m')
print('-='*10,'FIM DO PROGRAMA','-='*10)

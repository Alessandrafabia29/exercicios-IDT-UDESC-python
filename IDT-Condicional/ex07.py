print('-='*10,'PROGRAMA DATA NO FORMATO:dd/mm/aaaa','-='*10)
#entrada de dados
data = str(input('Digite uma data no formato dd/mm/aaaa: __/__/____'))
#fatiamento da string:extrai dia mês ano e converte para números
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])
#inicializa a variavel para dizer se a data é válida
valida = False
#verificação dos meses de 31 dias
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia >=1 and dia <= 31:
        valida = True
#verificação dos meses de 30 dias
if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia >= 1 and dia <= 30:
        valida = True
#verificação especial para fevereiro
#verificação do ano bissexto(divisível por 4 e não por 100,ou divisível por 400)
elif mes == 2:
    if(ano %4 ==0 and ano %100 != 0)or(ano % 400 == 0):
        if dia >=1 and dia <=29:
            valida = True
    else:
        if dia >=1 and dia <= 28:
            valida = True
#saída
if valida:
    print('A data é válida.')
else:
    print('Data Inválida.')
print('-='*10,'FIM DO PROGRAMA','-='*10)




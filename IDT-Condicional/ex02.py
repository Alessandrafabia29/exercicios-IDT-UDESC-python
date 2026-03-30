print('-='*10,'PROGRAMA REAJUSTE SALARIAL','-='*10)
#ENTRADA
salarioAtual = float(input('Informe seu salário atual: R$ '))
#Processamento
if salarioAtual < 280:
    percentualAumento =  (20/100) #20%
    aumento = percentualAumento * salarioAtual #20
    salarioNovo = salarioAtual + aumento
elif salarioAtual >= 280 and salarioAtual < 700:
    percentualAumento =  (15/100)
    aumento = percentualAumento * salarioAtual
    salarioNovo = salarioAtual + aumento
elif salarioAtual > 700 and salarioAtual < 1500:
    percentualAumento =  (10/100)
    aumento = percentualAumento * salarioAtual
    salarioNovo = salarioAtual + aumento
elif salarioAtual > 1500:
    percentualAumento =  (5/100)
    aumento = percentualAumento * salarioAtual
    salarioNovo = salarioAtual + aumento
    
#Saída
print(f'Seu salário atual R$ {salarioAtual}')
print(f'Seu percentual de aumento salarial {percentualAumento} %')
print(f'O valor do seu aumento de salário R$ {aumento:.2f}')
print(f'Seu novo salário após o reajuste R$ {salarioNovo}')
print('-='*10,'FIM DO PROGRAMA','-='*10)

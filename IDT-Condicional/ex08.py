print('-='*10,'PROGRAMA MATEMÁTICA','-='*10)
num = float(input('Informe um número:'))
#verificação se o número é par ou ímpar
if num % 2 == 0:
    print('O número informado é par.')
else:
    print('O número informado é ímpar.')
#verificação se o número é positivo ou negativo
if num > 0 :
    print('O número informado é positivo.')
else:
    print('O número informado é negativo.')
#verificação se o número é inteiro ou decimal
if num % 1 == 0:
    print('O número informado é inteiro.')
else:
    print('O número informado é decimal.')
print('-='*10,'FIM DO PROGRAMA','-='*10)

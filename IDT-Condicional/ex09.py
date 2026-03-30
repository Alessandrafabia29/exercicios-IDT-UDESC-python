print('-='*10,'PROGRAMA POSTO DE COMBUSTÍVEL','-='*10)
tipo = str(input('Informe o tipo de combustível: G-Gasolina/ A-Álcool: ')).upper()
litros = float(input('Informe a quantidade de litros:'))
if tipo == 'A':
    if litros <=20:
        pagar = litros * 4.90
        desconto = (3/100) * pagar
        total = pagar - desconto
    elif litros > 20:
        pagar = litros * 4.90
        desconto = (5/100) * pagar 
        total = pagar - desconto
else: # tipo == 'G':
    if litros <= 20:
        pagar = litros * 6.20
        desconto = (4/100) * pagar 
        total = pagar - desconto
    elif litros > 20:
        pagar = litros * 6.20
        desconto = (6/100) * pagar
        total = pagar - desconto
print(f'O valor total a pagar R$ {total}')
print('-='*10,'FIM DO PROGRAMA','-='*10)


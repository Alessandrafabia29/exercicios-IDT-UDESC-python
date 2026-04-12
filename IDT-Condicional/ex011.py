print('-='*10,'PROGRAMA SUPERMERCADO','-='*10)
#entradas
tipo = int(input('Digite o tipo da carne:[1]Filé Duplo [2]Alcatra [3]Picanha--'))
quantidade = float(input('Informe a quantidade: Kg'))
formaPagamento = int(input('Informe a forma de pagamento:[1]Dinheiro/Cartão [2]Cartão Fidelidade--'))
#processamento
nomeCarne = ''
if tipo == 1:
    nomeCarne = 'Filé Duplo'
    if quantidade <= 5:
        preço = 49.90
    else:
        preço = 39.80

elif tipo == 2:
    nomeCarne = 'Alcatra'
    if quantidade <=5:
        preço = 59.90
    else:
        preço = 49.89
    
elif tipo == 3:
    nomeCarne = 'Picanha'
    if quantidade <= 5:
        preço = 69.90
    else:
        preço = 59.80

#pagamento normal
pagamento = quantidade * preço
#pagamento com desconto
desconto = 0
if formaPagamento == 2:
    desconto = pagamento * (5/100)
    valorFinal = pagamento - desconto
else:
    valorFinal = pagamento

#saídas
print('CUPOM FISCAL:')
print(f'Tipo de carne: {nomeCarne}  ')
print(f'Quantidade: {quantidade} Kg')
print(f'Preço Total:Dinheiro/Cartão R${pagamento:.2f}')
print(f'Desconto:Exclusivo para cartão fidelidade R${desconto:.2f} ')
print(f'Valor Final: R$ {valorFinal:.2f}')
print('-='*10,'FIM DO PROGRAMA','-='*10)


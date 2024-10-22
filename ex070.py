total = totmil = menorPreco = cont = 0
barato = ''

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1

    if preco > 1000:
        totmil += 1

    if cont == 1 or preco < menorPreco:
        menorPreco = preco
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

print(f'O total da compra foi de R${total:.2f} ')
print(f'Temos {totmil} produtos custando mais que R$1000')
print(f'O produto mais barato foi {barato} e custou R${menorPreco:.2f}')

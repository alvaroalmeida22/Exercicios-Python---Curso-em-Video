dias = int(input('Quantos dias alugados? '))
rodagem = float(input('Quantos Km rodados? '))
dias = dias * 60
rodagem = rodagem * 0.15
total = dias + rodagem
print('O total a pagar é de R${:.2f}'.format(total))

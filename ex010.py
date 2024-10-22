reais = float(input('Quanto você tem na carteira? R$'))
dolares = reais/3.27
print('Com R${} você pode comprar US${:.2f}.'.format(reais, dolares))

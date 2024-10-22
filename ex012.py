valor = float(input('Qual é o preço do produto? R$'))
desconto = (5/100) * valor
novovalor = valor - desconto
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(valor, novovalor))

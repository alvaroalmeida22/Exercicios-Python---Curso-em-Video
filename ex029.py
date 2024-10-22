velocidade = int(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido de 80Km/h.')
    print('Você deve pagar uma multa de R${}.'.format((velocidade - 80) * 7))

print('Tenha um bom dia! Dirija com segurança!')
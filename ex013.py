salario = float(input('Qual é o salário do funcionário? R$'))
novosalario = salario + ((15/100) * salario)
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}.'.format(salario, novosalario))

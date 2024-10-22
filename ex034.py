salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250.00:
    print('Quem ganhava R${} passa a ganhar R${:.2f} agora.'.format(salario, salario+((15/100) * salario)))
else:
    print('Quem ganhava R${} passa a ganhar R${:.2f} agora.'.format(salario, salario+(1/10) * salario))

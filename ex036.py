casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
meses = anos * 12
prestacao = casa / meses
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestacao))
if (salario * (3/10)) >= prestacao:
    print('\033[1:32mEmpréstimo pode ser concedido!')
else:
    print('\033[1:31mEmpréstimo negado!')

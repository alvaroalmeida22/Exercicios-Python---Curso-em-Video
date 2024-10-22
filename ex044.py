print('\033[1:34m{:=^40}\033[m'.format(' LOJA DO SEU ALVARO '))
valor = float(input('Qual o preço das compras? R$'))
print('''\033[1:36mFORMAS DE PAGAMENTO\033[m
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão 
[ 3 ] 2x no cartão
[ 4 ] 3x ou mas no cartão''')
opcao = int(input('\033[1:31mQual a opção?\033[m '))
if opcao == 1:
    novo = valor - valor/10
    print('Sua compra terá um desconto de 10% e valerá R${}'.format(novo))
elif opcao == 2:
    novo = valor - valor/20
    print('Sua compra terá um desconto de 5% e valerá R${}'.format(novo))
elif opcao == 3:
    print('O valor de sua compra valerá R${} e cada parcela será de R${}'.format(valor, valor/2))
elif opcao == 4:
    novo = valor + valor/5
    parcelas = int(input('\033[1:33mQuantas parcelas? \033[m'))
    print('O valor de sua compra valerá R${} e cada parcela será de R${}'.format(novo, novo/parcelas))
else:
    print('\033[1:31mOpção INVÁLIDA de pagamento. Escolha uma opção válida.\033[m')

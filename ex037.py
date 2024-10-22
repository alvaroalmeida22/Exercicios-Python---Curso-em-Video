num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('\033[1:32m{}\033[m convertido para BINÁRIO é igual a \033[1:32m{}\033[m'.format(num , bin(num)[2:]))
elif opção == 2:
    print('\033[1:32m{}\033[m convertido para OCTAL é igual a \033[1:32m{}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('\033[1:32m{}\033[m convertido para HEXADECIMAL é igual a \033[1:32m{}\033[m'.format(num, hex(num)[2:]))
else:
    print('\033[1:31mOpção inválida! Tente novamente.')

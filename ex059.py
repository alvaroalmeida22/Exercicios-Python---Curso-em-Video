from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while not opção == 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('Qual a sua opção? '))
    if opção == 1:
        print('>>>>>>> A soma {} + {} = {}'.format(n1, n2, n1 + n2))


    elif opção == 2:
        print('>>>>>>> A multiplicação {} x {} = {}'.format(n1, n2, n1*n2))

    elif opção == 3:
        if n1 > n2:
            print('>>>>>>> O maior valor digitado entre {} e {} foi {}'.format(n1, n2, n1))

        else:
            print('>>>>>>> O maior valor digitado foi {}'.format(n2))

    elif opção == 4:
        print('Informe os números novamente...')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    else:
        print('Fim do programa! Volte sempre!')
    print('\033[1:31m=\033[m' * 40)
    sleep(2)
print('Opção inválida. Tente novamente.')
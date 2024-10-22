from random import randint
print('\033[1:33m-=\033[m' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('\033[1:33m-=\033[m' * 20)
soma = 0
contador = 0
while True:
    print('\033[1:34m-\033[m' * 40)
    computador = randint(1, 10)
    n = int(input('Diga o valor: '))
    escolha = input('Par ou Ímpar? [P/I] ').upper()
    soma = n + computador

    if soma % 2 == 0 and escolha == 'P':
        print(f'Você jogou {n} e o computador {computador}. A soma {soma}.')
        print('''Parabéns você VENCEU!
Vamos jogar novamente...''')
    elif soma % 2 == 1 and escolha == 'i':
        print(f'Você jogou {n} e o computador {computador}. A soma {soma}.')
        print('''Parabénste. você VENCEU!
                Vamos jogar novamente..''')
    elif soma % 2 == 0 and escolha == 'i':
        print(f'Você jogou {n} e o computador {computador}. A soma {soma}.')
        print('VOCÊ PERDEU!')
        break
    else:
        print(f'Você jogou {n} e o computador {computador}. A soma {soma}.')
        print('VOCÊ PERDEU!')
        break
    contador += 1
    print('\033[1:34m-\033[m' * 40)
print(f'\n\033[1:31mGAME OVER! Você venceu \033[m\033[1:32m{contador}\033[m \033[1:31mvez(es).')

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('\033[1:34m~\033[m' * 30)
    if n < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        print('\033[1:34m~\033[m' * 30)

        break
    i = 1
    for i in range(1,11):
        print(f'{i} x {n} = {i * n}')
    print('\033[1:34m~\033[m' * 30)

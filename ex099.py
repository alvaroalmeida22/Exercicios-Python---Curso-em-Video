from time import sleep

def maior(*num):
    cont = maior = 0
    print('-'*30)
    print('Analisando os valores passados...')
    print('|', end='')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        
        if valor > maior:
            maior = valor
    print('|', end='')
    print(f'\nO maior valor é {maior}')
    print('-'*30)
    print()

maior(7, 2, 9, 1)
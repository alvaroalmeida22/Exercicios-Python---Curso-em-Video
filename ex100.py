from random import randint
from time import sleep
numeros = []

def sorteia():
    print()
    print('-'*55)
    print(f'Sorteando os 5 valores da lista: ', end='')
    for n in range(0, 5):
        numero = randint(a=0, b=10)
        print(numero, end=' ', flush=True)
        sleep(0.5)
        numeros.append(numero)
    print('PRONTO!')
    print()
    
    
def somaPar():
    soma = 0
    for v in numeros:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {numeros} temos {soma}')
    print('-'*55)
    print()


sorteia()
somaPar()

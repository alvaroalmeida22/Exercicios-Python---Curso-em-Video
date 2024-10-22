from time import sleep
from random import randint
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual a sua jogada? '))
print('\033[1:31mJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!\033[m')
sleep(0.5)
print('\033[1:33m=-\033[m'*20)
computador = randint(0, 2)
if computador == 0:
    print('Computador jogou Pedra')
elif computador == 1:
    print('Computador jogou Papel')
else:
    print('Computador jogou Tesoura')
if jogada == 0:
    print('Jogador jogou Pedra')
elif jogada == 1:
    print('Jogador jogou Papel')
else:
    print('Jogador jogou Tesoura')
print('\033[1:33m=-\033[m'*20)
if jogada == computador:
    print('EMPATE!')
elif jogada == 0 and computador == 1:
    print('COMPUTADOR GANHOU!')
elif jogada == 0 and computador == 2:
    print('JOGADOR GANHOU!')
elif jogada == 1 and computador == 0:
    print('JOGADOR GANHOU!')
elif jogada == 1 and computador == 2:
    print('COMPUTADOR GANHOU!')
elif jogada == 2 and computador == 0:
    print('COMPUTADOR GANHOU!')
elif jogada == 2 and computador == 1:
    print('JOGADOR GANHOU!')

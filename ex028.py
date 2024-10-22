from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
usuario = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if usuario == computador:
    print('Parabéns! Você acertou!')
else:
    print('Que pena! O computador pensou em {} e vc escolheu {}'.format(computador, usuario))

from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'jogador 1' : randint(1, 6), 
             'jogador 2' : randint(1, 6),
             'jogador 3' : randint(1, 6),
             'jogador 4' : randint(1, 6)
             }


for k, v in jogadores.items():
    print(f'  => O {k} tirou {v}')
    sleep(1)
    
ranking = []

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('=-' * 30)

for i, v in enumerate(ranking):
    print(f'  => O {i+1}º foi: {v[0]} com {v[1]}')
    sleep(1)
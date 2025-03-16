ficha = {}
partidas = []

ficha['nome'] = str(input('Nome do jogador: '))

jogos = int(input(f'Quantas partidas {ficha["nome"]} jogou? '))

for c in range(0, jogos) :
    partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))

ficha['gols'] = partidas[:]
ficha['total'] = sum(partidas)

print('-='*30)
print(ficha)
print('-='*30)
for k, v in ficha.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)

print(f'O jogador {ficha["nome"]} jogou {len(ficha["gols"])} partidas')

for i, v in enumerate(ficha['gols']):
    print(f'Na partida {i+1}, fez {v} gols.')

print(f'Foi um total de {ficha["total"]} gols.')
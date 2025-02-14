numeros = [[], []]


for c in range(1, 8):

    resposta = int(input(f'Digite o {c}º valor: '))

    if resposta % 2 == 0:
        numeros[0].append(resposta)
    else:
        numeros[1].append(resposta)

print('-='*30)
print(f'Os valores pares digitados foram {sorted(numeros[0])}')
print(f'Os valores impares digitados foram {sorted(numeros[1])}')
print('-='*30)

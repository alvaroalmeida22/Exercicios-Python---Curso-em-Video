numeros= []
pares = []
impares = []

while True:
    numeros.append(int(input('Digite um número: ')))

    resposta = str(input('Quer continuar? [S/N]'))

    if resposta in 'Nn':
        break

for v in numeros:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'A lista completa é {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')

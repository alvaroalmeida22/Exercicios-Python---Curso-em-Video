matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
somaColuna3 = 0
maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}] [{c}]: '))

for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:    
            pares += matriz[l][c]
    print()

print('-='*30)
print(f'A soma de todos os números pares é: {pares}')

for l in range(0, 3):
        somaColuna3 += matriz[l][2]

print('-='*30)
print(f'A soma dos valores da terceira coluna é: {somaColuna3}')

for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print('-='*30)
print(f'O maior valor da segunda linha é: {maior}')
print('-='*30)

    
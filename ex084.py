infosGerais = []
dadosPessoais = []
maiorPeso = menorPeso = 0 

while True:
    dadosPessoais.append(str(input('Nome: ')))
    dadosPessoais.append(float(input('Peso: ')))

    if len(infosGerais) == 0:
        maiorPeso = menorPeso = dadosPessoais[1]
    else:
        if dadosPessoais[1] > maiorPeso:
            maiorPeso = dadosPessoais[1]
        if dadosPessoais[1] < menorPeso:
            menorPeso = dadosPessoais[1]

    infosGerais.append(dadosPessoais[:])
    dadosPessoais.clear()

    continuar = str(input('Quer continuar? [S/N] '))

    if continuar in 'Nn':
        break

print('-='*40)
print(f'Ao todo você cadastrou {len(infosGerais)} pessoas')

print(f'O maior peso foi {maiorPeso}Kg. Maior peso de ', end='')
for pessoa in infosGerais:
    if pessoa[1] == maiorPeso:
        print(f'{[pessoa[0]]}', end='')
print()
print(f'O menor peso foi {menorPeso}Kg. Menor peso de ', end='')
for pessoa in infosGerais:
    if pessoa[1] == menorPeso:
        print(f'{[pessoa[0]]}', end='')

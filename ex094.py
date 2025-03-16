pessoa = {}
galera = []
soma = media = 0 
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    print(galera)
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('-='*30)

print(f'A) Foram cadastradas {len(galera)} pessoas.')

media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f}')

print('C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p['nome']}, ', end='')

print()
print('D) Lista das pessoas que estão com a idade acima da média:')
for p in galera:
    if p['idade'] > media:
        for k, v in p.items():
            print(f'    {k} = {v}; ', end = '')
        print()


        
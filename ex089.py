ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome,[nota1, nota2], media])

    resposta = str(input('Quer continuar? S/N '))
    if resposta in 'Nn':
        break

print('-='*30)
print(f'{"Nº":<4}{"Nome":<20}{"Média":>8}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opcao == 999:
        print('Finalizando...')
        break
    if opcao <= len(ficha) - 1:
        print(f'O aluno {ficha[opcao][0]} teve as notas {ficha[opcao][1]}')
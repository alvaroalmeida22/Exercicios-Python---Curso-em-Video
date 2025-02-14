ficha = {}
ficha['nome'] = str(input('Nome: '))
ficha['media'] = float(input(f'Média de {ficha["nome"]}: '))
print('=-'*30)
""" print(f' - O nome é {ficha["nome"]}')
print(f' - A média é {ficha["media"]}') """

if ficha['media'] >= 7:
    ficha['situação'] =  'APROVADO'
elif 7 > ficha['media'] >= 6 :
    ficha['situação'] = 'RECUPERAÇÃO'
else:
    ficha['situação'] = 'REPROVADO'

for k, v in ficha.items():
    print(f' - O/A {k} é {v}')
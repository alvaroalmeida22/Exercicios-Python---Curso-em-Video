from datetime import datetime

ficha = {}

ficha['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
ficha['idade'] = datetime.now().year - nascimento
ficha['CT'] = int(input('Carteira de trabalho (0 não tem): '))

if ficha['CT'] != 0:
    ficha['ano contratacao'] = int(input('Ano de contratação: '))
    ficha['salario'] = float(input('Salário: '))
    ficha['aposentadoria'] = (((ficha['ano contratacao'] + 35) - datetime.now().year)) + ficha['idade']
    print('=-' * 30)

    for k, v in ficha.items():
        print(f'   ->  {k}: {v}')
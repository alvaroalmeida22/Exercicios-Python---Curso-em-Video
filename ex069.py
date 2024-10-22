cont_idade = 0
cont_homens = 0
cont_idade_mulheres = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    if idade > 18:
        cont_idade += 1
    sexo = str(input('Sexo: [M/F] ')).upper()[0]
    if sexo == 'M':
        cont_homens += 1
    if idade < 20 and sexo == 'F':
        cont_idade_mulheres += 1
    pergunta = str(input('Quer continuar? [S/N] ')).upper()
    if pergunta == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {cont_idade}
Ao todo temos {cont_homens} homens cadastrados
E temos {cont_idade_mulheres} mulher(es) com menos de 20 anos''')

int1 = int(input('Primeiro número inteiro: '))
int2 = int(input('Segundo número inteiro: '))
if int1 > int2:
    print('O primeiro valor é maior!')
elif int2 > int1:
    print('O segundo valor é maior!')
elif int1 == int2:
    print('Não existe valor maior, os dois são iguais!')

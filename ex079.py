valores = []

while True:
    valor = int(input('Digite um valor: '))

    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado!')
    else:
        print('Valor duplicado! Não será adicionado.')


    resposta = str(input('Quer continuar? [S/N]')).upper()

    if resposta == 'N':
        break
    
    
print('-'*50)
print(f'Você digitou os valores {sorted(valores)}')
print('-'*50)

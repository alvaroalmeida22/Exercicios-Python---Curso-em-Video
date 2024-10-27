valores =[]

while True:
    valores.append(int(input('Digite um valor: ')))

    resposta = str(input('Voc^deseja continuar? [S/N] '))

    if resposta in 'nN':
        break

print('-='*50)

print(f'Você digitou {len(valores)} elementos')

valores.sort(reverse=True)
print(f'Os valores em ordem descrescente são {valores}')

if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não está na lista!')

print('-='*50)

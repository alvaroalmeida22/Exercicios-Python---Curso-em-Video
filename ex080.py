valores = []

for v in range(0, 5):
    valor = int(input('Digite um valor: '))

    if v == 0 or valor > valores[-1]:
        valores.append(valor)
        print('Valor adicionado ao final da lista')
    else:
        posicao = 0
        while posicao < len(valores):

            if valor <= valores[posicao]:
                valores.insert(posicao, valor)
                print(f'Valor adicionado na posição {posicao} da lista')
                break
            posicao += 1
print(f'Os valores digitados em ordem foram {valores}')

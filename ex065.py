p = 'S'
s = cont = maior = menor = 0
if p in 'Ss':
    while p in 'Ss':
        n = int(input('Digite um número: '))
        p = input('Quer continuar? [S/N] ').upper().strip()[0]
        cont += 1
        s += n
        if cont == 1:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
print('Você digitou {} números e a média foi {:.2f}'.format(cont, s/cont))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))

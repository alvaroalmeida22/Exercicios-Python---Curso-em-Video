n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o ultimo número: '))
numeros = (n1, n2, n3, n4)

print(f'o número 9 apareceu {numeros.count(9)} vezes')

if 3 in numeros:
    print(f'O número 3 apareeu na {numeros.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')

print('Os números pares digitados são: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end =' ')

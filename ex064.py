n = 0
cont = 0
s = 0
n = int(input('Digite um número (999 para parar): '))
while n != 999:
    cont += 1
    s += n
    n = int(input('Digite um número (999 para parar): '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, s))

print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for PA in range(a1, a1+(r*10), r):
    print(PA, end=' -> ')
print('ACABOU!')

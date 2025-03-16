from time import sleep

def contador(inicio, fim, passo):
    print()
    print('-'*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        for c in range(inicio, fim+1, passo):
            print(c, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
        

    if inicio > fim:
        absoluto = abs(passo)
        for c in range(inicio, fim - 1, -absoluto):
            print(c, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
        print('-'*30)
        




contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f ,p)
print()

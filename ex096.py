def area(larg, comp):
    
    a = larg * comp

    print(f'A área de um terreno de {larg}m X {comp}m = {a}m²')

print('-'*20)
print('CONTROLE DE TERRENOS')
print('-'*20)

c = float(input('COMPRIMENTO (m): '))
l = float(input('LARGURA (m): '))
area(l, c)
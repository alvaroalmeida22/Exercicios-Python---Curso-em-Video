soma = 0
cont = 0
for c in range(3, 501, 2):
    if (c % 3) == 0:
        cont += +1
        soma += c
print('A soma dos \033[1:31m{} \033[mnúmeros divisíveis por 3 no intervalo de 1 a 500 é \033[1:32m{}\033[m.'.format(cont, soma))

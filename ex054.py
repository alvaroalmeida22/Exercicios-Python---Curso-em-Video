from datetime import date
atual = date.today().year
contmaior = 0
contmenor = 0
for c in range(1, 8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - nascimento
    if idade >= 21:
        contmaior += 1
    else:
        contmenor += 1
print('Ao todo tivemos {} pessoas \033[1:32mmaiores\033[m de idade'.format(contmaior))
print('e tembém {} pessoas \033[1:31mmenores\033[m de idade'.format(contmenor))

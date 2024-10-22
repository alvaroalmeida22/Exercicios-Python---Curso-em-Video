from random import randint
numero = randint(0, 10)
tentativas = 1
print('Sou seu computador... \n Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi?')
jogador = int(input('Qual é o seu palpite? '))
while jogador != numero:
    tentativas += 1
    if jogador < numero:
        print('Mais... Tente mais uma vez.')
        jogador = int(input('Qual é o seu palpite? '))
    else:
        print('Menos... Tente mais uma vez.')
        jogador = int(input('Qual é o seu palpite? '))
print('Acertou com {} tentativas. Parabéns!'.format(tentativas))

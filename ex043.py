peso = float(input('Qual é seu peso? (kg) '))
altura = float (input('Qual é a sua altura? (m) '))
imc = peso / pow(altura, 2)
print('\033[1:32mSeu IMC vale {:.2f}.\033[m'.format(imc))
if imc < 18.5:
    print('Você está \033[1:33mABAIXO DO PESO\033[m normal')
elif imc <= 25:
    print('O seu peso está \033[1:32mIDEAL!')
elif imc <= 30:
    print('Você está com \033[1:33mSOBREPESO!')
elif imc <= 40:
    print('Você está com \033[1:33mOBESIDADE!')
else:
    print('Você está com \033[1:31mOBESIDADE MÓRBIDA! CUIDADO!')

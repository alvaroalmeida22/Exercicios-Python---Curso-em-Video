from datetime import date
ano = int(input('Quando nasceu o atleta? '))
idade = date.today().year - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: \033[1:31mMIRIM')
elif 9 < idade <= 14:
    print('Classificação: \033[1:32mINFANTIL')
elif 14 < idade <= 19:
    print('Classificação: \033[1:33mJÚNIOR')
elif 19 < idade <= 25:
    print('Classificação: \033[1:34mSÊNIOR')
elif idade > 25:
    print('Classificação: \033[1:35mMASTER')

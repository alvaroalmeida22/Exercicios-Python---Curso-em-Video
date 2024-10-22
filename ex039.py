from datetime import date
nascimento = int(input('Se for mulher digite 0. Se for homem, digite seu ano de nascimento: '))
data = date.today().year
if nascimento == 0:
    print('\033[1:32mNo Brasil, mulheres não são obrigadas a se alistar!')
elif data - nascimento < 18:
    print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, data - nascimento, data))
    print('Ainda faltam {} anos para o alistamento.'.format(nascimento + 18 - data))
    print('Seu alistamento será em {}'.format(nascimento + 18))
elif data - nascimento > 18:
    print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, data - nascimento, data))
    print('Você ja deveria ter se alistado há {} anos.'.format(data - nascimento - 18))
    print('Seu alistamento foi em {}'.format(nascimento + 18))
else:
    print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, data - nascimento, data))
    print('Você tem que se alistar \033[1:31mIMEDIATAMENTE!')
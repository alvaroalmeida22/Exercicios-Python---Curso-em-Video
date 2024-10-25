numeros = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:

    usuario = int(input('Digite um número entre 0 e 20: '))
    
    if usuario > 20 or usuario < 0:
        print('Tente novamente.')

    else: 
        print(f'Você digitou o número {numeros[usuario]}')
        break
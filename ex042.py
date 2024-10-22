a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if a == b == c:
         print('\033[1:35mEQUILÁTERO.')
    elif a == b or a == c or b == c:
        print('\033[1:33mISÓSCELES')
    else:
        print('\033[1:34mESCALENO')
else:
    print('Os segmentos acima \033[1:31mNÃO PODEM FORMAR\033[m um triângulo')

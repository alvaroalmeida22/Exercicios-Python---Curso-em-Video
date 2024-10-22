a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos acima \033[1:32mPODEM\033[m formar um triângulo.')
else:
    print('Os segmentos acuima \033[1:31mNÃO\033[m podem formar um triângulo.')

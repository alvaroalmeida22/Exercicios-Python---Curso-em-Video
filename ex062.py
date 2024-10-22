p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 0
m = 1
c3 = 0

while c <= 9:
    print(p, end=' -> ')
    p += r
    c += 1
print('PAUSA')
while m != 0:
    m = int(input('Quantos termos você quer mostrar mais? '))
    if m != 0:
        c2 = 1
        while m >= c2:
            print(p, end=' -> ')
            p += r
            c2 += 1
            c3 += m

        print('PAUSA')

    else:

        print('Progressão finalizada com {} termos mostrados.'.format(c + c3 - 2))

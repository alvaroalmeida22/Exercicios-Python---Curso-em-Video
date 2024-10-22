p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 1
while c <= 10:
    print(p, end=' -> ')
    p += r
    c += 1
print('PAUSA')
m = 1
c2 = 1
while m != 0:
    m = int(input('Quantos termos você quer mostrar mais? '))
    if m != 0:
        while m >= c2:
            print(p, end=' -> ')
            p += r
            c2 += 1
        print('PAUSA')
    else:
        print('Progressão finalizada com {} termos mostrados.'.format(c + c2 - 2))

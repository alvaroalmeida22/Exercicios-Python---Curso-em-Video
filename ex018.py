from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
print('O ângulo de {} tem o seno de {:.2f}'.format(ang, seno))
cosseno = cos(radians(ang))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ang, cosseno))
tangente = tan(radians(ang))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ang, tangente))

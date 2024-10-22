largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2
print('Sua parede tem dimensão de {}m x {}m e sua área é de {:.3f}m²'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {:.2f}L de tinta'.format(tinta))

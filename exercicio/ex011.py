larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2
print('A area é de {:.2f}m². vai precisar de {:.2f}L litros de tintas.'.format(area, tinta))
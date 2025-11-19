'''opos = float(input('Comprimento do cateto oposto: '))
adja = float(input('Comprimento do cateto adjacente: '))
hipo = (opos ** 2 + adja ** 2) ** (1/2)
print('A hipotenusa é {:.2f}'.format(hipo))'''
#outra forma

'''import math
opos = float(input('Comprimento do cateto oposto: '))
adja = float(input('Comprimento do cateto adjacente: '))
hipo = math.hypot(opos, adja)
print('A hipotenusa é {:.2f}'.format(hipo))'''
#outra forma

from math import hypot
opos = float(input('Comprimento do cateto oposto: '))
adja = float(input('Comprimento do cateto adjacente: '))
hipo = hypot(opos, adja)
print('A hipotenusa é {:.2f}'.format(hipo))
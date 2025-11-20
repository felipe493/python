'''import math
angulo = float(input('Digite a ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem o seno de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))'''
#outra forma

from math import radians, sin, cos, tan
angulo = float(input('Digite a ângulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {} tem o seno de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))
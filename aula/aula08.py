'''
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é iqual a {:.2f}'.format(num, math.floor(raiz)))
'''
#outra maneira de importa
'''
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é iqual a {}'.format(num, floor(raiz)))
'''

import random
num = random.randint(1, 10)
print(num)
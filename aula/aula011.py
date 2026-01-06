#print('\033[4;30;45mOlá, mundo!\033[m')

#outra forma de colorar Cores no Terminal
'''a = 2
b = 3
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))'''

#outra forma de colorar Cores no Terminal
'''nome = 'Felipe'
print('Ola! Mundo prezer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))'''

#outra forma de colorar Cores no Terminal
nome = 'Felipe'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Ola! Mundo prezer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
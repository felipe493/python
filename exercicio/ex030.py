numero = int(input('Me diga um número qualquelr: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} ÍNPAR'.format(numero))
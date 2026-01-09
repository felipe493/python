num = int(input('Digitem um número inteiro: '))
print('''Escolar uma das bases para converção' 
[ 1 ] coverter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} covertido para BINÁRIO é iqual a {}'.format(num, bin(num) [2:]))
elif opção == 2:
    print('{} convertido para OCTAL é iqual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é iqual a {}'.format(num, hex(num) [2:]))
else:
    print('Opção inválidar. tente novamente.')
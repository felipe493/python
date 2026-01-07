casa = float(input('Valor da casa?  R$'))
salario = float(input('Salario do comprador? R$'))
ano = int(input('Quantos anos de financiamento? '))
prestacao = casa / (ano * 12)
minimo = salario * 0.30
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de {:.2f}'.format(casa, ano, prestacao))
if prestacao <= minimo:
    print('O empréstimo foi CONCEDIDO!')
else:
    print('O empréstimo foi NEGADO!')
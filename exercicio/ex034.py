salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 0.15)
else:
    novo = salario + (salario * 0.10)
print('Quem ganhava R${:.2f} passa a ganha R${:.2f} agora.'.format(salario, novo))

''' outra forma de calcular
salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganha R${:.2f} agora.'.format(salario, novo))'''
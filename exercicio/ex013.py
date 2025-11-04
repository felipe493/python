salar = float(input('Qual o salário do fucionário? R$'))
novo = salar + (salar * 15 / 100)
print('O fucionário que ganhava R${}, com aumento de 15%, passou a ganha R${:.2f} '.format(salar, novo))
preco = float(input('Qual o preço do produto? R$'))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custa R${:.2f}'.format(preco, novo))
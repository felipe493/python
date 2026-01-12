nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segundanota: '))
media = (nota1 + nota2) / 2
if 6 > media >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif media < 5:
    print('O aluno está REPROVADO.')
elif media >= 6:
    print('O aluno está APROVADO.')
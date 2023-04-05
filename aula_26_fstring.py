# x ou X = hexadecimal
# > esquerda
# < direita
# ^ centro
# !r é método __repr__ - conversion flag
# !s é método __str__ - conversion flag
# !a é método __ascii__ - conversion flag

variavel = 'abc'

print(f'{variavel}')
print(f'{variavel: >10}') # preenche com 10 espaços à esquerda
print(f'{variavel: <10}.') # preenche com 10 espaços à direita
print(f'{variavel: ^10}.') # poe o texto no centro

print(20*'_')

print(f'{50.57979874465:.1f}') # define quantidade de casas decimais a ser exibidas
print(f'{50.57979874465:+.1f}') # o + exibe se o numero é positivo ou negativo
print(f'O hexadecimal de 1500 é: {1500:08X}')

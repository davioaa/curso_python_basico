# try tenta executar o código || caso ocorra qualquer erro
# except -> icirrey algum erro ao tentar executar
# excessão = erros no programa que param a execução.

numero_str = input('Dobrarei o numero digitado:')

#if numero_str.isdigit():
#    numero_float = float(numero_str)
#    print(f'O dobro do {numero_str} é {numero_float * 2}.')
#else:
#    print('Isso não é um numero.')

try: # tente executar
    numero_float = float(numero_str) # caso seja digitado uma letra, ele pula para o except
    print(f'O dobro do {numero_str} é {numero_float * 2:.1f}.')
except: # se ocorrer algum erro dentro do try, o código pula imediatamente para o except.
    print('Isso não é um numero.')

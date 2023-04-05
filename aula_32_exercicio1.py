numero = eval(input('Insira um numero inteiro'))

if type(numero) == int:
    if (numero%2==0):
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é ímpar')
else:
    print('O numero digitado não é inteiro')
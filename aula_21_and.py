entrada = input('[e]ntrar ou [s]air:\n')
senha = input('Digite sua senha: \n')
senha_permitida = '1234'

if entrada == 'e' and senha == senha_permitida: # operador logico and
    print('Bem vindo ao sistema\n')
elif entrada == 's':
    print('Você saiu do sistema.\n')
else:
    print('Não foi possível realizar sua autenticação.')
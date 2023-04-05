# estruturas condicionais
# if, elif, else
# elif == else if da linguagem C
entrada = input('Digite "a" para entrar ou "z" para sair\n') # entrada

#lembrar se sempre por os : após a operação logica
if entrada == 'a': # caso sim
    print('Você entrou no sistema\n')
elif entrada == "z": # caso nao
    print('Você saiu do sistema\n')
else: #qualquer outro caso
    print('Erro')

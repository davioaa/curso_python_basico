#strings em python são iteraveis
#in = entre
# caso algo esteja in/entre os nomes, retorna true, caso contrario, false.
nome = 'Davi'

#print(nome[2]) #acessa o índice 2, nesse caso, o 'v'

print('v' in nome) #se v estiver entre nome, retorna true
print('r' in nome) # se r estiver entre nome, retorna true, nesse caso, retorna false

print(10 * "_")

print('v' not in nome) # se v nao estiver no nome = true, nesse caso, retorna false
print('r' not in nome) # se r nao estiver no nome = true

nome_entrada = input('Digite seu nome: ')
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome_entrada:
    print(f'{encontrar} esta em {nome_entrada}')
else:
    print(f'{encontrar} não está em {nome_entrada}')
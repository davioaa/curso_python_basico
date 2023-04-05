nome = 'Davi'

tamanho_nome = len(nome)
nome_final = ''

i = 0
while i < tamanho_nome:
    print(f'*{nome[i]}*')
    nome_final += '*' + nome[i]
    i += 1

print(nome_final)
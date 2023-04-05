# imprime repetidas vezes enquanto determinada condição for verdadeira

condicao = True

while condicao:
    nome = input('Digite seu nome: ')

    if nome == 'sair':
        break # encerra o laço, independente de onde esteja

print('Acabou')
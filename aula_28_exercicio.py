nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if (nome != '') & (idade != ''):
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}') # inverte a string
    if ' ' in nome: # se conter espaço...
        print('Seu nome contém espaço')
    else:
        print('Seu nome não contém espaço')
    print(f'Seu nome possui {len(nome)} letras') # mostra quantidade de letras usando len
    print(f'A primeira letra do seu nome é {nome[0]}') # primeiro indice sempre 0
    print(f'A ultima letra do seu nome é {nome[-1]}') # ultimo indice sempre -1
else:
    print("Desculpe, você deixou campos vazios.")
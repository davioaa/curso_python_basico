nome = input('Digite seu nome: \n')

tamanho_nome = len(nome)

NOME_PEQUENO = (tamanho_nome <= 4)
NOME_MEDIO = (tamanho_nome == 5) or (tamanho_nome == 6)
NOME_GRANDE = (tamanho_nome > 6)

if NOME_PEQUENO:
    print(f'{nome}, seu nome é curto')
elif NOME_MEDIO:
    print(f'{nome}, seu nome é normal')
elif NOME_GRANDE:
    print(f'{nome}, seu nome é muito grande')
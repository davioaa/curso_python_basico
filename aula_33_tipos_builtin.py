"""
Dados imutáveis: str, int, float, bool | tais dados tambem sao consederados OBJETOS
Ações podem ser executadas a partir dos objetos.
Ações são chamadas de métodos e podem ser encontradas na documentação da linguagem.
https://docs.python.org/pt-br
"""
string = "Davi" # este valor é imutável
outra_variavel = f'{string[:2]}mudei_a_string{string[3:]}' # so pode ser alterado a partir da formatação
# {string[:3]} imprime os indices de 0 à 2 (o ultimo indice nao é impresso)


print(string[2]) # o 'v' não pode ser alterado por outro valor
print(outra_variavel.zfill(20)) # exemplo de método
# while / else

string = 'valor'

i = 0

while i < len(string):
    letra = string[i]

    print(letra)
    i += 1

else:
    print('O else foi executado') # o else é executado após a finalização do laço do while.
    # caso haja um break no while, o else não é executado.
'''
iterável -> str, range, etc (possuem metodo ___iter___)
Iterador -> quem sabe entregar um item por vez
next -> entrega o proximo item
iter -> entrega objeto iterador
'''

texto = iter('Davi') 
print(next(texto)) # passa pelo primeiro item
print(next(texto)) # passa pelo segundo item
print(next(texto)) # passa pelo terceiro item
print(next(texto)) # passa pelo quarto item
# print(next(texto)) # apresenta um erro ao esgotar os valores

...

# for letra in palavra # ao setar esta linha de codigo o seguinte acontece:
 
palavra = 'Palavra' # iteravel
iterator = iter(palavra) # iterator

while True: # um laço de repetição é criado até não haver mais itens iteráveis na variavel
    try:
        letra = next(iterator)
        print(letra)
    except StopIteration: # a linha de codigo sera executada exclusivamente se o erro for este
        break
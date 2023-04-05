# # duas variaveis com o mesmo valor
# # podem ser identificadas pelo mesmo id

# v1 = 'a'
# v2 = 'a'

# print(id(v1))
# print(id(v2))

# # duas variaveis com o mesmo lugar na memoria



# Flag - Marcar um local
# None = Não Valor
# is e is not = É ou não é um valor, tipo, identidade
# id = Identidade
condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faz Algo')
else:
    print('Faz nada')

print(passou_no_if, passou_no_if is None) # retorma uma condição lógica
print(passou_no_if, passou_no_if is not None)
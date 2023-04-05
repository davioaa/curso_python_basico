nome = 'Davi Oliveira'
peso = 80
altura = 1.70
imc = peso / altura ** 2

print(f'Seu nome é {nome}, voce tem {peso} quilos e')
print(f"seu imc é: {imc:.2f}") # :. somado ao valor, limita quantidade de casas decimais.


a = 1
b = 2
c = 3
print("a = {} | b = {} | c = {}".format(a, b, c)) # para formatar basta inserir dentro das chaves
print("a = {:.2f} | b = {:.5f} | c = {:.4f}".format(a, b, c)) # formatado
print("a = {0:.2f} | b = {1:.5f} | c = {2:.4f}".format(a, b, c)) # é possível inserir por índices

 # é possível inserir parametros às variáveis
print("a = {indice_1:.2f} | b = {indice_2:.5f} | c = {indice_3:.4f}"
.format(
    indice_1 = a, indice_2 = b, indice_3 = c # as variaveis são transformadas em parametros
    ))
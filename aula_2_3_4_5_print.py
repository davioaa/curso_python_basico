# sep altera a forma como cada dado aparecerá
print(30, 11, 2022, sep="/") # sepaador /
print(20, 16, 35, sep=":") # separador :

# end altera como o final do codigo será formatado
# por padrão ele entre com um \n para quebra de linha
# porem é possivel alterar

print(1, 2, 3, sep="_", end="\n") # como seria se fosse exibido o padrão python
print(4, 5, 6, sep="_", end="\ncoe\n") # não há mais quebra de linha

# classe type exibe o tipo de dado

print(type("String")) #str
print(type(1)) # int
print(type(1.1)) # float
print(type(10 == 10)) # bool

#dados tambem podem ser booleanos
# True ou False

print(10 == 10)
print(10 == 11)
print(10 != 10)

# há precedencia de operadores
# primeiro é executado os parenteses (n)
# depois a exponenciação **
# depois a divisão, multiplicação, resto e divisão inteira * / // %
# apos soma e subtração + -


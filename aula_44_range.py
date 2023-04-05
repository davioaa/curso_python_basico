# range é um iteravel
# nao depende do for, nem o for depende do range
# range(start, stop, step)
# quando é incluido apenas um valor, é o valor de stop
# o ultimo digito não é incluído

numeros = range(10) # define somente stop
# numeros = range(5, 10) # define start e stop
# numeros = range(5, 10, 2) # define start, stop e o passo(step)

for numero in numeros:
    print(numero)
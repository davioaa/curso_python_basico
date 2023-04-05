# comando realiza input de dados, sempre em forma de string,
# caso seja nececssário realizar cálculos, é neccessário converter o tipo de dado.
nome = input('Qual o seu nome?\n')
print(f'Olá, {nome}')

# escrito dessa forma, mostra a variável e o valor contido na mesma.
print(f'Olá, {nome=}') # util para ver variavel

numero_1 = input('Digite um número\n')
print(type(numero_1)) # tipo string
int_numero_1 = int(numero_1) # converte para inteiro
print(type(int_numero_1)) # tipo inteiro
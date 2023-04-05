hora = eval(input('Insira o horário atual em numeros inteiros'))

manha = (hora >= 0) and (hora < 12)
tarde = (hora >= 12)
noite = (hora >= 18) and (hora < 23)

if manha:
        print('Bom dia!')
elif tarde:
        print('Boa tarde!')
elif noite:
        print('Boa Noite!')
else: 
        print('Não conheço essa hora')

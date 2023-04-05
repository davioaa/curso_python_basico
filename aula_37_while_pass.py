contador = 0

while contador < 100:
    contador += 1

    if contador == 6:
        continue # pula para a próxima repetição.

    if contador >= 10 and contador <= 26: # vai pular o 10 e o 26
        continue

    print(contador)


    if contador == 40:
        break # para a repetição por completo.

print('Finalizado!')
print ('--------------------------')
print ('   Alistamento militar   ')
print ('--------------------------')
idade = int(input('Quantos anos você tem? '))
if idade == 18:
    print ('Você está na idade correta para se alistar.')
elif idade < 18:
    tempo = (idade - 18) * (-1)
    print ('Você ainda não está na idade para se alistar, faltam {} anos'.format(tempo))
else:
    tempo = idade - 18
    print ('Já passaram {} anos do seu tempo de alistamento'.format(tempo))


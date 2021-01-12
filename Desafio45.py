
import random
print ('--------------------')
print ('      Jokenpô')
print ('--------------------')
usuario = str(input('Digite sua escolha: '))
lista = ['PEDRA','PAPEL', 'TESOURA']
escolhido = random.choice(lista)
print ('O computador escolheu {}'.format(escolhido))
if usuario == 'papel' and escolhido == 'TESOURA':
    print ('O computador venceu :(')

elif escolhido == 'PAPEL' and usuario == 'tesoura':
    print ('Você venceu!!!')

elif escolhido == 'TESOURA' and usuario == 'pedra':
    print ('Você venceu!!!')


elif escolhido == 'PEDRA' and usuario == 'tesoura':
    print ('O computador venceu :(')

elif escolhido == 'PAPEL' and usuario == 'pedra':
    print ('O computador venceu :(')

elif escolhido == 'PEDRA' and usuario == 'papel':
    print ('Você venceu!!!')
else:
    print ('Houve um empate')
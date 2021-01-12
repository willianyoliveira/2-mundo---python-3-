print ('--------------------')
print ('    Pagamento')
print ('--------------------')
valor = float(input('Digite o valor do produto: '))
print ('Se o pagamento for:\n à vista no dinheiro ou cheque  : a \n à vista no cartão : b \n em até 2x no cartão : c \n em 3x ou mais no cartão: d ')
condicao = str(input('Digite a letra correspondente a forma de pagamento: \n'))
if condicao == 'a':
    total = valor - (valor * (10/100))
    print ('Você receberá um desconto de 10%. Valor a pagar {}'.format(total))
elif condicao == 'b':
    total = valor - (valor * (5/100))
    print ('Você receberá um desconto de 5%. Valor a pagar {}'.format(total))
elif condicao == 'c':
    total = valor 
    print ('Valor a pagar {}'.format(total))
else:
    total = valor + (valor * (20/100))
    print ('Haverá um acrescimo de 20% no valor total. Valor a pagar {}'.format(total))
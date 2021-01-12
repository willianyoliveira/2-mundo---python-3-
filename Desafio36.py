print ('--------------------------')
print (' Financiamento de Moradia ')
print ('--------------------------')
valor = float(input('Qual o valor do imóvel que você gostaria de comprar? \n'))
sal = float(input('Qual o seu salário atual? \n'))
anos = int(input('Em quantos anos você gostaria de pagar o imóvel? \n'))
prestacao = valor/(anos*12)
print ('O valor da prestação mensal será de {:.2f} reais, durante  {} anos \n'.format(prestacao, anos))
if prestacao > sal*(30/100):
    print ('Você não poderá comprar o imóvel, pois a prestação implicaria em 30% do seu salário.')
    print ('Aumente a quantidade de anos para realizar uma nova análise.')
else:
    print('Parabéns você poderá comprar o imóvel')

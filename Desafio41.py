print ('----------------------------------')
print (' Confederação nacional de natação')
print ('----------------------------------')
nome = str(input('Digite seu nome:  \n'))
idade = int(input('Digite sua idade:  \n'))
if idade <= 9:
    print ('{}, você está inscrito na categoria MIRIM'.format(nome))
elif idade > 9 and idade <=14:
    print ('{}, você está inscrito na categoria INFANTIL'.format(nome))
elif idade >14 and idade <= 19:
    print ('{}, você está inscrito na categoria JÚNIOR'.format(nome))
elif idade > 19 and idade<=20:
    print ('{}, você está inscrito na categoria SÊNIOR'.format(nome)) 
else:
    print ('{}, você está inscrito na categoria MASTER'.format(nome))


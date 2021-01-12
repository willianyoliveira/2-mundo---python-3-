print ('----------------------------------')
print ('    Índice de massa corporal')
print ('----------------------------------')
nome = str(input('Digite seu nome: \n'))
altura = float(input('Digite sua altura: \n'))
peso = float(input('Digite seu peso: \n'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print ('Olá {}, seu IMC é {:.2f}. Você está abaixo do peso ideal'.format(nome, imc))
elif imc >= 18.5 and imc < 25:
    print ('Olá {}, seu IMC é {:.2f}. Você está no peso ideal'.format(nome, imc))
elif imc >= 25 and imc < 30:
    print ('Olá {}, seu IMC é {:.2f}. Você está com sobrepeso'.format(nome, imc))
elif imc >= 30 and imc < 40:
    print ('Olá {}, seu IMC é {:.2f}. Você está em obesidade'.format(nome, imc))
else:
    print ('Olá {}, seu IMC é {:.2f}. Você está em obesidade mórbida'.format(nome, imc))
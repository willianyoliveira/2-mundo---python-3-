print ('--------------------------')
print ('  Comparador de números ')
print ('--------------------------')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print ('O número {} é maior que o número {}'.format(num1, num2))
elif num2 > num1:
    print ('O número {} é maior que o número {}'.format(num2, num1))
else:
    print ('Os dois números digitados são iguais')
num = int(input('Digite um número inteiro: '))
print (''' Escolha uma das bases para conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
opcao = int(input('Digite sua opçaõ: '))
if opcao == 1:
    print ('A conversão do número {} para binário, é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print ('A conversão do número {} para binário, é igual a {}'.format(num, hex(num)[2:]))
elif opcao == 3:
    print ('A conversão do número {} para binário, é igual a {}'.format(num, oct(num)[2:]))
else:
    print ('Opção inválida, tente novamente!')
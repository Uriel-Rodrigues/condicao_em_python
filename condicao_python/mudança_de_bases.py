#programa que pede um numero inteiro, e pede para escolher a base de conveção
# 1 para binario
# 2 para octal
# 3 para hexadecimal

numero = int(input('digite o numero para se convertido: '))
print('agora escolha uma das opções para escolher a base para converter\n')

print(' - - - - menu de escolhas - - - - -')
print('| [1] CONVERTER PARA BINARIO      |')
print('| [2] CONVERTER PARA OCTAL        |')
print('| [3] CONVERTER PARA HEXADECIMAL  |')
print('- - - - - - - - - - - - - - - - - -\n')

escolha = int(input('escolha sua opção: '))

if (escolha == 1):
    print('\n o numero {} em binario corresponde a {}'.format(numero, bin(numero)[2:]))

elif (escolha == 2):
    print('0 numero {} em octal corresponde a {}'.format(numero, oct(numero)[2:]))

elif (escolha == 3):
    print('o numero {} em hexadecimal corresponde a {}'.format(numero, hex(numero)[2:]))

else:
    print('opção invalida por favor escolher uma das opções do menu')
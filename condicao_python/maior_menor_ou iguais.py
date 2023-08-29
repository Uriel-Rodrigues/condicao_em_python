#promaga que lê 2 numero e compare e mostre uma das menagens:
# o perimero valor é maior
#n  segundo valor é maior
# os dois valores são iguais

n1 = int(input('digite o primeiro numero para comparar: '))
n2 =  int(input('digite o segundo numero para comparar: '))

if (n1 > n2 ):
    print('\no primeiro valor {} é maior que o segundo {}'.format(n1, n2))

elif(n2 > n1):
    print('\no segundo valor {} é maio que o primeiro {}'.format(n2, n1))

else:
    print('\nnao existe valor maior ou menor pois os 2 são iguais')

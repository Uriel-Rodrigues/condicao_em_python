#programa que le os lados de um triangulo e mostra o seu tipo
#equilatero: todos os lados iguais
#isosceles:dois lados iguais
#escaleno:todos os lados diferentes

l1 = int(input('digite o tamanho do primeiro lado: \n'))
l2 = int(input('digite o tamanho do segundo lado: \n'))
l3 = int(input('digite o tamanho do terceiro lado: \n'))

if(l1 < l2 + l3 and l2 < l1 + l2 and l3 < l1 + l2):
    print('os seguimentos podem formar um triangulo')
    if (l1 == l2 == l3):
        print('voce tem um triangulo EQUILATERO')

    elif (l1 == l2 or l1 == l3 or l3 == l2 ):
        print('voce tem um triangulo ISOSCELES')

    elif (l1 != l2 != l3 != l1):
        print('voce tem um triangulo ESCALENO')
else:
    print('as medidas nao podem formar um triangulo')
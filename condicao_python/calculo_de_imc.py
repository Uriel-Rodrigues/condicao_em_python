#programa que calcula o IMC de alguem
#abaixo de 18.5 : abaixo do peso
#entre18.5 e 25: peso ideal
#25 ate 30 sobrepeso
#30 ate 40 obesidade
#acima de 40 obesidade morbida

#peso/altura*altura

print('|----- calculo do IMC -----|')
print('|          peso            |')
print('|     ---------------      |')
print('|     altura * altura      |')
print('|--------------------------|\n')

altura = float(input('digite a sua altura em METROS: \n'))
peso = float(input('digite o seu peso em KG: \n'))

calculo = peso/(altura*altura)

if (calculo < 18.4):
    print('seu peso é de {:.2f}, voce precisa se alimentar melhor, esta abaixo do peso'.format(calculo))

elif (18.5 <= calculo >= 25):
    print('seu peso é de {:.2f}, continue assim voce esta no seu peso ideial'.format(calculo))

elif (26 <= calculo >= 30):
    print('seu peso é de {:.2f}, vishh... vc esta precisando se alimentar melhor, esta acima do seu peso '.format(calculo))

elif (31 <= calculo >= 40):
    print('seu peso é de {:.2f}, voce realmente precisa se alimentar melhor voce esta acima do obeso'.format(calculo))

elif (calculo > 41):
    print('seu peso é de {:.2f},  voce esta precisando de dieta imediata, esta com obesidade morbida'.format(calculo))
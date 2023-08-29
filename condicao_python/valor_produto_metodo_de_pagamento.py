'''programa que calcula o valor a ser pago por um produto considerando o seu preço normal
e condição de pagamento
 - dinheiro ou cheque : 10% de disconto
 - avista no cartão : 5%
 - em ate 2x no cartão: preço normal
 - 3x ou mais: 20% de juros'''

preço = float(input('digite o valor do roduto: '))
print('|----------MENU DE PAGAMENTO-----------|')
print('| [1] pagamento em dinheiro ou cheque  |')
print('| [2] pagamento avista no cartão       |')
print('| [3] pagamento em 2x no cartão        |')
print('| [4]pagamento em 3x ou mais no cartão |')
print('|--------------------------------------|\n')

escolha = int(input('qual a sua escolha da forma de pagamento: '))

if (escolha == 1):
    print('voce escolheu a opção {} e seu pagamento tem 10% de desconto'.format(escolha))
    desconto = preço - ((10 * preço)/100)
    print('novo valor a ser pago é de {}'.format(desconto))

elif(escolha == 2):
    print('voce escolheu a opção {} e su pagamneto tem 5% de desconto'.format(escolha))
    desconto = preço - ((5 * preço)/100)
    print('novo valor a ser pago é de {}'.format(desconto))

elif (escolha == 3):
    print('voce escolheu a opção {} e seu pagamento corresponde ao valor normal do produto'.format(escolha))
    print('valor a ser pago {}'.format(preço))
    parcelas = preço/2
    print('2x de {}'.format(parcelas))

elif(escolha == 4):
    print('voce escolheu a opção {} e seu pagamneto tem um juros de 20% no valor total'.format(escolha))
    juros = ((20 * preço)/100) + preço
    nparcelas = int(input('digite o numero de parcelas: '))
    vparcelas = juros/nparcelas
    print('valor a ser pago {}'.format(juros))
    print('em {}x de {}'.format(nparcelas, vparcelas))

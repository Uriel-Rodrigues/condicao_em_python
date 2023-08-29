#programa para aprovar a compra de uma casa
#perguntar o preço da casa
#salario do comprador
#quanto anos ele vai pagar
#calcular prestação mençal, nao pode exeder 30% ou o emprestimo sera negado

salario = float(input(' informar salario do comprador: '))
preçocasa = float(input('\n informar o valor da casa: '))
tempopagamento = int(input('\n informar tempo de pagamento em anos: '))

porcentagemsalario = (30 * salario)/100
pagamentomeses = tempopagamento * 12
prestação = preçocasa/pagamentomeses

if(prestação > porcentagemsalario):
    print('\n sinto muito mas a prestação axede 30% do seu salario \n')
    print('voce nao pode financiar essa casa, mostraremos outros produtos \n')
else:
    print('seu finaciamento foi aprovado, ficamos felizes pela preferencia')



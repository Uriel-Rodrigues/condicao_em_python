#programa que faça o  compudador jogar jokenpo com voce
from random import choice
from time import sleep

opções = ['pedra', 'papel', 'tesoura']

print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
print('|             JOKENPO!             |')
print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')

print('seja bem vindo ao jokenpo!')
print('sera que vc aceita o desfio de jogar contra o seu proprio PC?')

resposta = str(input('aceita o desafio? sim ou nao: '))

if ('sim' in resposta):
    print('muito bem! vamos jogar! J-O-K-E-N-P-O!')
    print('escolhendo...')
    sleep(2)
    escolhapc = choice(opções)
    print('escolhi!')

    print('sua vez escolha o seu')
    escolhausu = str(input('qual sua escolha? digite aqui: '))

    print('muito bem! vamos la!')
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')

    if (escolhapc == 'pedra' and escolhausu == 'papel'):
        print('pc escolheu: {}'.format(escolhapc.upper()))
        print('usuario escolheu: {}'.format(escolhausu.upper()))
        print('USUARIO GANHOU!')
        print('VOCÊ GANHOU DESSA VEZ')

    elif(escolhapc == 'pedra' and escolhausu == 'tesoura'):
        print('pc escolheu: {}'.format(escolhapc.upper()))
        print('usuario escolheu: {}'.format(escolhausu.upper()))
        print('PC GANHOU!')
        print('HAHA EU GANHEI')

    elif (escolhapc == 'papel' and escolhausu == 'tesoura'):
        print('pc escolheu: {}'.format(escolhapc.upper()))
        print('usuario escolheu: {}'.format(escolhausu.upper()))
        print('USUARIO GANHOU!')

    elif (escolhapc == 'papel' and escolhausu == 'pedra'):
        print('pc escolheu: {}'.format(escolhapc.upper()))
        print('usuario escolheu: {}'.format(escolhausu.upper()))
        print('PC GANHOU!')
        print('HAHA EU GANHEI')

    elif (escolhapc == 'tesoura' and escolhausu == 'papel'):
        print('pc escolheu: {}'.format(escolhapc.upper()))
        print('usuario escolheu: {}'.format(escolhausu.upper()))
        print('PC GANHOU!')
        print('HAHA EU GANHEI')

    elif (escolhapc == 'pedra' and escolhausu == 'pedra'):
        print('EMPATE!')
    elif (escolhapc == 'tesoura' and escolhapc == 'tesoura'):
        print('EMPATE!')
    elif (escolhapc == 'papel' and escolhausu == 'papel'):
        print('EMPATE!')

else:
    print('\nsem problemas, jogamos outro dia')

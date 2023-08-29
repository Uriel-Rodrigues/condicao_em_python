#programa que leia a idade de alguem e diga:
#se ainda vai se alistar
#se é hora de se alistar
#ja passou o tempo de se alistar
#o programa deve mostrar o tempo que falta ou o que ja passou
from datetime import date

anoatual = date.today().year
anonascimento = int(input('digite o seu ano de nascimento: '))
idade = anoatual - anonascimento

if (idade > 18):
    saudo = idade - 18
    print('ja passou {} anos do tempo de se alistar'.format(saudo))

elif (idade < 18):
    saudo = 18 - idade
    print('ainda nao esta no momento de se alistar, ainda falta {} anos'.format(saudo))

elif(idade == 18):
    print('ja esta na hora de se alistar voce tem exatamente 18 anos')

#programa que leia o ano de nacimento de um atleta e diga sua categoria de acordo com a idade
#ate 9 anos :MIRIN
#ate 14 anos : INFANTIL
#ate 19 anos : JUNIOR
#ate 20 anos : SÊNIOR
#acima: MASTER
from datetime import date
print('bem vindo a seleção de natação!\n')
anoatual = date.today().year
nascimento = int(input('digite seu ano de nascimento: '))
idade = anoatual - nascimento

if (idade <= 9):
    print('parabens! voce tem {} anos e esta escalado na categoria MIRIN'.format(idade))
    print('BOA SORTE!')

elif (10 <= idade <= 14):
    print('PARABEN! voce tem {} anos e esta escalado na categocria INFANTIL'.format(idade))
    print('BOA SORTE!')

elif (15 <= idade <= 19 ):
    print('PARABENS voce tem {} anos e esta escalado na categoria JUNIOR'.format(idade))
    print('BOA SORTE!')

elif (idade == 20):
    print('PARABENS voce tem {} anos e esta escalado na categoria SÊNIOR'.format(idade))
    print('BOA SORTE!')

elif (idade > 20):
    print('PARABEND voce tem {} anos e esta escalado na categoria MASTER'.format(idade))
    print('BOA SORTE!')

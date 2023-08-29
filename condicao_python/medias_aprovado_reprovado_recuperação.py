#programa que calcule a media de um aluno e mostre uma mensagem dependendo da sua media
#media abaixo de 5.0 : reprovado
#media entre 5.0 e 6.9: recuperação
#media 7.0 ou superior: aprovado

nota1 = float(input('digite a primeira nota do aluno: '))
nota2 = float(input('digite a segunda media do aluno: '))
nota3 = float(input('digite a terceira media do aluno: '))

media = (nota1 + nota2 + nota3)/3

if (media < 5.0):
    print('\nmedia do aluno foi {} aluno reprovado'.format(media))

elif (5.0 <= media <= 6.9 ):
    print('\nmedia do aluno foi {} aluno em recuperação'.format(media))

elif (media >= 7.0):
    print('\nmedia do aluno foi {} aluno aprovado'.format(media))


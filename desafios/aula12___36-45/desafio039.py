#Faça um programa que leia o ano de um nascimento de um jovem e informe, de acordo com a sua idade: Se ele ainda vai se alistar ao serviço militar; Se é a hora de se alistar; Se já passou do tempo do alistamento; Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
ano = int(input('Qual o ano do seu nascimento? '))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
#idade = 2021 - ano
if idade < 18:
    menor = 18 - idade
    saldo = atual + menor
    print('Seu alistamento seá em {}.'.format(saldo))
    print('Você ainda não tem 18 anos, falta {} anos para se alistar!'.format(menor))
elif idade == 18:
    print('Você tem 18 anos, tem que se alistar ainda esse ano!')
elif idade > 18:
    maior = idade - 18
    saldo = atual - maior
    print('Você já passou da idade, deveria ter se alistado há {} anos atrás.'.format(maior))
    print('Seu alistamento foi em {}.'.format(saldo))

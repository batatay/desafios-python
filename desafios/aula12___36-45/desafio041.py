#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: Até 9 anos: MIRIM; Até 14 anos: INFANTIL; Até 19 anos: JUNIOR; Até 20 anos: SÊNIOR; Acima: MASTER
ano = int(input('Qual o ano do seu nascimento? '))
idade = 2021 - ano
if idade <= 9:
    print('Você tem {} anos e está na categoria MIRIM!'.format(idade))
elif idade <= 14:
    print('Você tem {} anos e está na categoria INFANTIL!'.format(idade))
elif idade <= 19:
    print('Você tem {} anos e está na categoria JUNIOR!'.format(idade))
elif idade <= 20:
    print('Você tem {} anos e está na categoria SÊNIOR!'.format(idade))
elif idade > 20:
    print('Você tem {} anos e está na categoria MASTER!'.format(idade))


#'''Até 9 anos: MIRIM;
'''Até 14 anos: INFANTIL; <=
Até 19 anos: JUNIOR; <=
Até 20 anos: SÊNIOR; <=
Acima: MASTER''''''>
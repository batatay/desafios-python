#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 1- A média de idade do grupo; 2- Qual é o nome do homem mais velho; 3- Quantas mulheres têm menos de 20 anos.
soma = 0
media = 0
maior = 0
velho = ''
menos = 0
for contador in range(1, 5):
    print('{} PESSOA: '.format(contador))
    nome = str(input('NOME: ')).strip().upper()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [F][M]: '))
    soma = soma + idade
    if contador == 1 and sexo in 'Mm':
        maior = idade
        velho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        velho = nome
    if sexo in 'Ff' and idade < 20:
        menos = menos + 1
media = soma / 4
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho é o {} e ele tem {} anos.'.format(velho, maior))
print(' {} Mulheres têm MENOS de 20 anos. {}.'.format(menos))
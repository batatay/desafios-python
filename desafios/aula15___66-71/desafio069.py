#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos; B) quantos homens foram cadastrados; C) quantas mulheres tem menos de 20 anos.
maior = macho = menos = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'FMfm':
        sexo = str(input('Digite o sexo [F]/[M]: ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        macho += 1
    if sexo == 'F' and idade < 20:
        menos += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S]/[N]: ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'Ao total foram: \n{maior} pessoas com mais de 18 anos; \n{macho} homens registrados; \n{menos} mulheres com menos de 20 anos.')

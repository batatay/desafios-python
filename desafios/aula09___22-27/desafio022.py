#Crie um programa que leia o nome completo de uma pessoa e mostre: >O nome com todas as letras maiúsculas; O nome com todas as letras minúsculas; Quantas letras ao todo sem considerar espaços; Quantas letras tem o primeiro nome.
#nome = str(input('Digite seu nome completo: '))
#print('Nome Maiúsculo: {}'.format(nome.upper()))
#print('Nome Minúsculo: {}'.format(nome.lower()))
#corte = nome.split()
#contagem = corte[0]
#print('Total de letras: {}'.format(len(nome)))
#print('Seu primeiro nome tem: {} letras'.format(len(corte[0])))
#print(corte)

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome... ')
print('Seu nome maiúsculo: {}'.format(nome.upper()))
print('Seu nome minúsculo: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem: {} letras'.format(nome.find(' ')))



#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome. / true ou false
nome = str(input('Digite seu nome: ')).strip()
print('SILVA' in nome.upper())
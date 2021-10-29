#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
ano = int(input('Digite um ano para saber se é BISSEXTO: '))
if ano % 4 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} não é BISSEXTO!'.format(ano))

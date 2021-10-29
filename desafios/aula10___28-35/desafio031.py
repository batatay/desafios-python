#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200Km e R$0,45 para viagens mais longas.
viagem = float(input('Quantos Km que você percorreu na viagem? '))
curta = viagem * 0.50
longa = viagem * 0.45
if viagem <= 200:
    print('O valor a ser pago é de: R$ {}'.format(curta))
else:
    print('O valor a ser pago é de: R$ {}'.format(longa))

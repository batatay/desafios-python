#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Digite o nome de uma cidade: '))
dividindo = cidade.split()
maiusculo = cidade.upper()
final = cidade.find('SANTO')
print('O primeiro nome da cidade é: {}'.format(dividindo[0]))
print('Ou seja, é {} afirmar que começa com "SANTO"'.format('SANTO' in maiusculo))

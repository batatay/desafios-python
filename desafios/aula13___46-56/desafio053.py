#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. EX: APOS A SOPA / A SACADA DA CASA / A TORRE DA DERROTA / O LOBO AMA O BOLO / ANOTARAM A DATA DA MARATONA
frase = str(input('Digite uma frase: ')).strip().upper()
separar = frase.split()
juntar = ''.join(separar)
inverter = ''
for contador in range(len(juntar)-1, -1, -1):
    inverter = inverter + juntar[contador]
print('{} invertida é {}'.format(juntar, inverter))
if inverter == juntar:
    print('A frase digitada É UM PALÍNDROMO!'.format(frase))
else:
    print('A frase digitada NÃO É PALÍNDROMO'.format(frase))

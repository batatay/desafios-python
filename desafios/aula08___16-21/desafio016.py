#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção de Inteira. Ex: Digite um número: 6.127 O número 6.127 tem a parte Inteira 6.
import math
numR = float(input('Digite um número: '))
print('Número real {}, sua porção inteira é {}'.format(numR, math.trunc(numR)))

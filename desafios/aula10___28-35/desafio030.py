#Crie um programa que  leia um número inteiro e mostre na tela se ele é par ou impar.
num = int(input('Digite um número inteiro para saber se é par ou impar: '))
divi = num % 2
if divi == 0:
    print('É par!')
else:
    print('É ímpar!')

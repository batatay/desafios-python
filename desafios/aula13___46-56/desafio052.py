#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número: '))
s = 0
for contador in range(1, num + 1):
    if num % contador == 0:
        s = s + 1
if s == 2:
    print("O número {} É PRIMO.".format(num))
else:
    print("O número {} NÃO É PRIMO.".format(num))
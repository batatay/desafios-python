#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
s = 0
for contador in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        s = s + num
print('A soma dos número pares digitados é: {}'.format(s))

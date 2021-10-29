#faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
n1 = int(input('Digite um número inteiro: '))
a = n1 + 1
s = n1 - 1
print ('O sucessor de {} é: {}\nE o antecessor de {} é: {}'.format (n1, a, n1, s))
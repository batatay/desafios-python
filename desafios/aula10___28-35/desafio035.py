#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
lado1 = float(input('Digite o primeiro comprimento da reta: '))
lado2 = float(input('Digite o segundo comprimento da reta: '))
lado3 = float(input('Digite o terceiro comprimento da reta: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os comprimentos PODEM formar um triângulo!')
else:
    print('Os comprimentos NÃO podem formar um triângulo!')

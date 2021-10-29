#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math
cat = float(input('Digite o comprimento do cateto oposto: '))
cad = float(input('Digite o comprimento do adjacente: '))
hip = math.hypot(cat, cad)
print('A hipotenusa vai medir {:.2f}'.format(hip))

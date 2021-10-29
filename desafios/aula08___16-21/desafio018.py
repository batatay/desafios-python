#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang = float(input('Digite o ângulo: '))
sen = math.sin(math.degrees(ang))
cos = math.cos(math.degrees(ang))
tan = math.tan(math.degrees(ang))
#print('O angulo de {} tem: seno, cosseno e tangente {}'.format(ang, se))
print('O ângulo de {} tem: \nO SENO de: {:.2f}\nO COSSENO de: {:.2f} \nE a TANGENTE de: {:.2f}'.format(ang, sen, cos, tan))
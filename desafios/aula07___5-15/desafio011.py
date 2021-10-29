#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessaria para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
n1 = float(input('Digite o número da largura da parede: '))
n2 = float(input('Digite o número da altura da parede: '))
m1 = n1 * n2
m2 = m1 / 2
print('A área é de: {}m²! \nSerão necessárias {} litros de tinta!'.format(m1, m2))


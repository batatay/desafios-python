#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$1,00=R$3,27
n1 = float(input('Por favor informe o valor em Reais que deseja converter em Dólares: '))
n2 = n1 / 5.05
print('Com R${} você pode comprar US${:.2f}!'.format(n1, n2))

#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
n1 = float(input('Digite o valor do seu produto: '))
n2 = n1 - (n1 * 5 / 100)
print('Seu produto está com um desconto de 5%. O valor atual do seu produto é de: {}'.format(n2))
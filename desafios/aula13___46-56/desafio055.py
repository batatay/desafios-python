#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menos peso lidos.
maior = 0
menor = 0
for contador in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: Kg '.format(contador)))
    if contador == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg \nO menor peso lido foi de {}Kg'.format(maior, menor))

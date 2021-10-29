#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
menor = 0
maior = 0
for contador in range(0, 7):
    ano = int(input('Digite o ano do seu nascimento: '))
    idade = atual - ano
    if idade < 18:
        menor = menor + 1
    else:
        maior = maior + 1
print('{} pessoas já atingiram a maior idade, e {} ainda não atingiram.'.format(maior, menor))
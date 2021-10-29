#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
termo = int(input('Digite o Primeiro termo: '))
razao = int(input('Digite a Razão: '))
print('Os 10 primeiros termos dessa progressão são:')
s = termo + (10 - 1) * razao
for contador in range(termo, s + razao, razao):
    print('{}'.format(contador), end=' / ')
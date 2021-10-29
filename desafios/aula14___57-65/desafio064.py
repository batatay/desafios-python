#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles. (desconsiderando o flag).
print('Digite 999 para parar!')
num = contador = soma = 0
while num != 999:
    num = int(input('Digite um número: '))
    soma += num
    contador += 1
print(f'Você digitou {contador - 1} números e a soma dos números digitados é de: {soma - 999}.')
#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
stop = 'S'
soma = valores = media = maior = menor = 0
while stop in 'Ss':
    num = int(input('Digite um número inteiro: '))
    soma += num
    valores += 1
    if valores == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    stop = str(input('Quer continuar? [S]/[N] ')).strip().upper()
media = soma / valores
print(f'Você digitou {valores} números e a média entre eles é de {media}')
print(f'O maior número digitado foi {maior} e o menor foi {menor}')
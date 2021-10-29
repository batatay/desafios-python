#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: A) Qual é o total gasto na compra. B) quantos produtos custam mais de R$1000; C) Qual é o nome do produto mais barato.
total = caro = menor = contador = 0
barato = ''
while True:
    nome = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto: R$ '))
    contador += 1
    total += preço
    if preço > 1000:
        caro += 1
    if contador == 1:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja adicionar mais itens? [S]/[N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('{:=^50}'.format(' NOTAS FINAIS '))
print(f'Total gasto na compra foi de: R${total}')
print(f'{caro} produtos custam mais de R$1000')
print(f'{barato} é o produto mais barato.')
print('=' * 50)

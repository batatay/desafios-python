#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
termo = int(input('Digite o Primeiro termo: '))
razao = int(input('Digite a Razão: '))
primeiro = termo
contador = 1
while contador <= 10:
    print(f'{primeiro}/', end='')
    primeiro += razao
    contador += 1

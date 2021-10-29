#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disse que quer mostrar 0 termos.
termo = int(input('Digite o Primeiro termo: '))
razao = int(input('Digite a Razão: '))
primeiro = termo
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{primeiro}/', end='')
        primeiro += razao
        contador += 1
    print('...')
    print('=*=' * 10)
    mais = int(input('Deseja mostrar mais quantos termos? '))
print('FIM..!')

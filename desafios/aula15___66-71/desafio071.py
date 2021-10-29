#crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('{:=^50}'.format(' CAIXA ELETRÔNICO '))
valor = int(input('Digite o valor que deseja sacar: RS ' ))
total = valor
reais = 50
resultado = 0
print('-' * 20)
while True:
    if total >= reais:
        total -= reais
        resultado += 1
    else:
        if resultado > 0:
            print(f'{resultado} cédulas de R${reais}')
        if reais == 50:
            reais = 20
        elif reais == 20:
            reais = 10
        elif reais == 10:
            reais = 1
        resultado = 0
        if total == 0:
            break
print('-' * 20)
print('{:=^50}'.format(' FIM '))
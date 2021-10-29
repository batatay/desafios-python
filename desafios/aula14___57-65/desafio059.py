#Crie um programa que leia dois valores e mostre um menu na tela: [1] somar; [2] multiplicar; [3] maior; [4] novos números; [5] sair do programa; Seu programa deverá realizar a operação solicitada em cada caso.
menu = 0
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
while menu != 5:
    print('=-=' * 10)
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    print('=-=' * 10)
    menu = int(input('O que deseja fazer? '))
    print('=*=' * 10)
    if menu == 1: #somar
        soma = num1 + num2
        print(f'Resultado da SOMA: {soma}')
    elif menu == 2: #multiplicar
        multi = num1 * num2
        print(f'Resultado da MULTIPLICAÇÃO: {multi}')
    elif menu == 3: #maior
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'O maior é {maior}')
    elif menu == 4: #novos numeros
        print('Ok, informe os novos números a seguir: ')
        num1 = float(input('Primeiro número: '))
        num2 = float(input('Segundo número: '))
    elif menu == 5:
        break
    else:
        #print('-' * 15)
        print('ERROR! Opção inválida. Escolha entre 1 e 5!')
        print('=*=' * 15)
print('FIM...!')
#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitória consecutivas que ele conquistou no final do jogo.
import random
final = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = random.randint(0, 11)
    total = jogador + computador
    resultado = ' '
    while resultado not in 'PpIi':
        resultado = str(input('Par ou impar? [P]/[I] ')).strip().upper()[0]
    print('=*=' * 10)
    print(f'Você jogou {jogador} e o computador {computador} \nO RESULTADO É {total}')
    print('=*=' * 10)
    if resultado == 'P':
        if total % 2 == 0:
            print('[ DEU PAR]')
            print('>>>>> YOU WIN!!')
            final += 1
        else:
            print('[ DEU ÍMPAR ]')
            print('>>>>> YOU LOSER!')
            break
    elif resultado == 'I':
        if total % 2 == 1:
            print('[ DEU ÍMPAR ]')
            print('>>>>>> YOU WIN!!!')
            final += 1
        else:
            print('[ DEU PAR ]')
            print('>>>>> YOU LOSER!')
            break
    print('=*=' * 10)
    print('Vamos jogar outra?')
print('=*=' * 10)
print(f'[ GAME OVER..!!! ]\nVocê venceu {final} vezes.')
print('=*=' * 10)

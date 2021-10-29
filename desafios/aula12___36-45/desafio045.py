#Crie um programa que faça o computador jogar Jokenpô com você.
import random
print('Vamos brincar de jokenpô ??? \nDigite: \n0 para "PEDRA" \n1 para "PAPEL" \n2 para "TESOURA"')
jogador = int(input('Qual é a sua escolha? '))
lista = ('PEDRA', 'PAPEL', 'TESOURA')
computador = random.randint(0, 2)
print('Você jogou {} e o computador {}'.format(lista[jogador], lista[computador]))
if computador == 0:
    if jogador == 0:
        print('HOUVE UM EMPATE')
    if jogador == 1:
        print('VOCÊ GANHOU!!!')
    if jogador == 2:
        print('VOCÊ PERDEU!')
elif computador == 1:
    if jogador == 0:
        print('VOCÊ PERDEU!')
    if jogador == 1:
        print('HOUVE UM EMPATE')
    if jogador == 2:
        print('VOCÊ VENCEU!!!')
elif computador == 2:
    if jogador == 0:
        print('VOCÊ VENCEU!!!')
    if jogador == 1:
        print('VOCÊ PERDEU!')
    if jogador == 2:
        print('HOUVE UM EMPATE')

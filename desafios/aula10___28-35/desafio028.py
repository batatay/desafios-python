#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
comput = int(input('Digite um número entre 0 e 5 e veja se consegue descobrir o número que o computador está pensando: '))
sorteio = random.randint(0, 5)
if comput == sorteio:
    print('YOU WIN! O número que o computador pensou foi {}!'.format(sorteio))
else:
    print('YOU LOSER! O número pensado foi: {}!'.format(sorteio))

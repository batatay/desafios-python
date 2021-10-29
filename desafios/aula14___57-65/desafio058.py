#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
comput = random.randint(0, 10)
#print(comput)
palpites = 0
player = int(input('Digite sua jogada: '))
while comput != player:
    comput = random.randint(0, 10)
    #print(comput)
    player = int(input('YOU LOSER! Tente novamente: '))
    palpites += 1
    if player == comput:
        print(f'>>>"YOU WIN"!!!<<<\nVocê digitou {player} e o computador {comput}.\nNÚMERO DE TENTATIVAS: {palpites + 1}')
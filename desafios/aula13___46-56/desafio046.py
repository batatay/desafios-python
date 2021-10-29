#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import time
print('CONTAGEM PARA O ESTOURO DE FOGOS: ')
for contador in range(10, 0, -1):
    time.sleep(1)
    print(contador)
print('FIIIIIU !!! BUMMMMM!!  POOOOW')
#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
import random
sorteio = random.randint(1, 5,), random.randint(1, 5,), random.randint(1, 5,), random.randint(1, 5,), random.randint(1, 5,)
print(f'Números sorteados:')
for num in sorteio:
    print(f'{num} ', end=' ')
print(f'\nO maior número sorteado foi {max(sorteio)}\nE o menor número sorteado foi {min(sorteio)}')


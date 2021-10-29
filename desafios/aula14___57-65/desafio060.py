#Faça um programa que leia um número qualquer e mostre seu fatorial. EX: 5! = 5x4x3x2x1=120.
num = int(input('Digite um número para saber seu fatorial: '))
fator = num
resultado = 1
print(f'{num}!= ', end='')
while fator > 0:
    print(f'{fator}', end='')
    print('x' if fator > 1 else '= ', end='')
    resultado *= fator
    fator -= 1
print(f'{resultado}')

#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: Equilátero: todos os lados iguais; Isósceles: dois lados iguais; Escaleno: todos os lados diferentes
lado1 = float(input('Digite o primeiro comprimento da reta: '))
lado2 = float(input('Digite o segundo comprimento da reta: '))
lado3 = float(input('Digite o terceiro comprimento da reta: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os comprimentos PODEM formar um triângulo: ')
    if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
        print('Equilátero')
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Os comprimentos NÃO podem formar um triângulo!')


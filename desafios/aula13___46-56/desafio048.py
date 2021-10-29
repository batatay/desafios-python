#Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontrarem no intervalo de 1 até 500.
s = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        s = s + num
print('A soma entre os números ímpares multiplos de três é: {}'.format(s))
#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) Quantas vezes apareceu o valor 9.; B) Em que posição foi digitado o primeiro valor 3; C) Quais foram os números pares.
num = (int(input('Digite um número: ')),
       int(input('Digite o segundo número: ')),
        int(input('Digite o terceiro número: ')),
         int(input('Digite o quarto número: ')))
print(f'Você digitou: \n{num}')
print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 apareceu na posição {num.index(3)+1}.')
else:
    print('O número 3 não foi digitado nenhuma vez!')
print('Os números pares digitados foram: ')
for par in num:
    if par % 2 == 0:
        print(par, end=' ')
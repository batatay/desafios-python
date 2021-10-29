#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário; 2 para octal; 3 para hexadecimal
num = int(input('Digite um número: '))
print('Deseja converter para: \n [1] Binário \n [2] Octal \n [3] Hexadecimal')
escolhido = int(input('Qual opção desejada? '))
if escolhido == 1:
    print('O número {} em Binário é {}'.format(num, bin(num)))
elif escolhido == 2:
    print('O número {} em Octal é {}'.format(num, oct(num)))
elif escolhido == 3:
    print('O número {} em Hexadecimal é: {}'.format(num, hex(num)))
else:
    print('ERROR! Escolha entre 1 e 3!')

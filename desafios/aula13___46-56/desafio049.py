#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input('Digite um número para saber a tabuada: '))
for contador in range(1, 11):
    print('{} x {:2} = {}'.format(num, contador, num*contador))

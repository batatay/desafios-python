#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o numero solicitado for negativo.
contador = 0
while True:
    num = int(input('Digite um número para saber a tabuada: '))
    print('=*=' * 10)
    if num < 0:
        break
    for contador in range(1, 11):
        print('{} x {:2} = {}'.format(num, contador, num*contador))
    print('=*=' * 10)
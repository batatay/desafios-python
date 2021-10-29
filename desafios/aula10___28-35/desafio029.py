#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite
velocidade = int(input('Em que velocidade você estava? '))
multa = 80
sub = velocidade - multa
resultado = sub * 7
if velocidade > multa:
    print('Você foi multado! A sua multa é de R${}'.format(resultado))
else:
    print('Não há multa!')

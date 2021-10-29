#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km1 = float(input('Quantos Km você percorreu com o carro? '))
dias = float(input('Por quantos dias ficou com o carro alugado? '))
kmRodados = km1 * 0.15
dUsados = dias * 60
resultado = kmRodados + dUsados
print('O valor total a ser pago é {}'.format(resultado))

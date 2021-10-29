#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.
m = int(input('Informe o valor em metros que deseja converter: '))
cm = m * 100
mm = m * 1000
print('{} Metros são: {} centímetro e {} milímetros'.format(m, cm, mm))
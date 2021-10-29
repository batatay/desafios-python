#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF
tempCelsius = float(input('Informe a temperatura em Celsius: '))
tempF = tempCelsius * 1.8 + 32
print('A temperatura de {}ºC equivale a {}ºF'.format(tempCelsius, tempF))
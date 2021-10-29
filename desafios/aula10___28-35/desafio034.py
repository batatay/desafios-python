#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite o valor do seu sálario: R$ '))
aumento1 = salario + (salario * 10 / 100)
aumento2 = salario + (salario * 15 / 100)
if salario > 1250:
    print('Você teve um aumento de 10%. Seu salário é de: {}'.format(aumento1))
else:
    print('Você teve um aumento de 15%. Seu salário é de: {}'.format(aumento2))

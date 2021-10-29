#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestaçao mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado.
casa = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Qual é o seu salário? R$ '))
anos = int(input('Em quantos anos deseja pagar? '))
mensal = casa / (anos * 12)
emprestimo = salario * 30 / 100
if mensal <= emprestimo:
    print('Seu empréstimo foi aceito. O valor a ser pago todo mês é de: R$ {:.2f} '.format(mensal))
else:
    print('Seu empréstimo foi negado!')

#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre o seu status, de acordo com a tabela abaixo: - IMC abaixo de 18,5: Abaixo do Peso; - Entre 18,5 e 25: Peso Ideal; - 25 até 30: Sobrepeso; - 30 até 40: Obesidade; - Acima de 40: Obesidade Mórbida.
peso = float(input('Digite o seu peso: Kg '))
altura = float(input('Digite a sua altura: M '))
imc = peso / (altura ** 2)
print('Seu IMC é de: {:.1f}'.format(imc))
if imc <18.5:
    print('Você está ABAIXO DO PESO.')
elif imc >=18.5 <25:
    print('Você está no PESO IDEAL!')
elif imc >=25 <30:
    print('Você está com SOBREPESO.')
elif imc >=30 <=40:
    print('Você está com OBESIDADE.')
elif imc >40:
    print('Você está com OBESIDADE MÓRBIDA')

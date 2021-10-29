#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Qual é o seu sexo? [M]/[F] ')).strip().upper()
while sexo not in 'FfMm':
        sexo = str(input('ERROR!!! \nDIGITE SOMENTE M OU F: \n[M] para masculino e [F] para feminino!: '))
print(f'Sexo informado: {sexo}. OK')
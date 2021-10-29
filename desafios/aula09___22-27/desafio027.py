#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. Ex: Ana Maria de Souza./ primeiro: Ana / último: Souza
nome = str(input('Digite seu nome completo: '))
separado = nome.split()
print('Primeiro nome: {}'.format(separado[0]))
#print('Último nome: {}'.format(separado[5]))
ultimo = separado.pop()
print('Último nome: {}'.format(ultimo))
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
t = float(input('Digite sua nota do teste: '))
p = float(input('Agora digite sua nota da prova: '))
s = t + p
r = s / 2
print('a soma das notas é: {} \nMédia final é: {}'.format(s, r))
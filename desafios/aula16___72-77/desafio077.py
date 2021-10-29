#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('cavalo', 'bolo', 'gato', 'cachorro', 'cadeira', 'banana', 'mesa', 'copo', 'janela', 'garrafa')
for cont in palavras:
    print(f'\nAs vogais da palavra {cont.upper()} são: ')
    for letra in cont:
        if letra in 'aeiou':
            print(f' "{letra}" ', end=' ')

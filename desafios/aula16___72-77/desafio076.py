#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
lista = ('Caderno', 22.50,
         'Caneta', 2,
         'Lápis', 1.50,
         'Estojo', 10.90,
         'Borracha', 1,
         'Mouse', 49.50,
         'Teclado', 10.90,
         'Água', 2.50)
print('=' * 40)
print('{: ^40}'.format(' LISTA DE PREÇOS: '))
print('=' * 40)
for cont in range(0, len(lista)):
    if cont % 2 == 0:
        print(f'{lista[cont]:.<30}', end='')
    else:
        print(f'R${lista[cont]:>6.2f}')
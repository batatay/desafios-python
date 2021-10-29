#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: - à vista dinheiro/cheque: 10% de desconto; - à vista no cartão: 5% de desconto; - em até 2x no cartão: preço normal; - 3x ou mais no cartão: 20% de juros.
produto = float(input('Digite o valor do seu produto: R$ '))
print('Formas de pagamento abaixo: \n[1] -> "À vista em dinheiro ou cheque" \n[2] -> "À vista no cartão" \n[3] -> "2x no cartão" \n[4] -> "3x ou mais no cartão" ')
pag = int(input('Digite forma de pagamento com o número indicado: '))
if pag == 1:
    total = produto - (produto * 10 / 100)
    print('Você tem um desconto de 10% e seu produto está custando {}R$'.format(total))
elif pag == 2:
    total = produto - (produto * 5 /100)
elif pag == 3:
    total = produto
    parcela = produto / 2
    print('Sua compra será parcelada em 2x de R${:.2f}, sem juros no cartão.'.format(parcela))
elif pag == 4:
    total = produto + (produto * 20 / 100)
    numparcelas = int(input('Dedeja parcelar em quantas vezes? '))
    parcela = total / numparcelas
    print('Sua compra será parcelada em {}x de R${:.2f} com juros no cartão.'.format(numparcelas, parcela))


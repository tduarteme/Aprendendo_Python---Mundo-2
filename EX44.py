"""Elabore um programa que calcule o valor a ser pago por um produto, 
   considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros"""


preco = float(input("Informe o preço do produto: "))

print (""" Opções de Pagamento:
      
      [1] - à vista dinheiro/PIX: 10% de desconto.
      [2] - à vista no cartão: 5% de desconto.
      [3] - em até 2x no cartão: preço formal.
      [4] - 3x ou mais no cartão: 20% de juros. """)

escolha = int(input("Digite a opção desejada: "))

if escolha == 1:
    cupom10 = preco - ((preco*10)/100)
    print("EBAA, ganhou 10% de desconto, pagará R${:.2f}" .format(cupom10))

elif escolha == 2:
    cupom5 = preco - ((preco*5)/100)
    print("Você ganhou 5% de desconto, pagará R${:.2f}" .format(cupom5))

elif escolha == 3:
    parcela2x = (preco/2)
    print("Optou em parcelar em 2x, pagará R${:.2f}/mês" .format(parcela2x))

elif escolha == 4:
    parcela3x = preco + ((preco*20)/100)
    print("Optou em parcelar em 3x, haverá um acréscimo de 20%, pagará R${:.2f}" .format(parcela3x))





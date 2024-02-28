"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
   Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
   A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""

# Exemplo de como inserir cores: ("\033[0;33;44mInforme o valor do Imóvel: R$ \033[m"))

imovel = float(input("Informe o valor do Imóvel: R$ "))
salario = float(input("Informe a renda do comprador: R$ "))
tempo = int(input("Anos de financiamento: "))

prestacao = imovel / (tempo*12)
porcentagem = salario*30/100

if prestacao <= porcentagem:
    print("Obaa, Financiamento \033[1;32;40mAPROVADO!\033[m A prestação será de R$ {:.2f}.".format(prestacao))

else:
    print("O valor da prestação será de R$ {:.2f}, infelizmente foi \033[1;31;40m NEGADO! \033[m".format(prestacao))




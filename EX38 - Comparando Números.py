"""Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais"""

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro númeor inteiro: "))

if num1 > num2:
    print("O número {} é maior!".format(num1))

elif num2 > num1:
    print("O número {} é o maior!".format(num2))

else:
    print("Ambos são iguais!")

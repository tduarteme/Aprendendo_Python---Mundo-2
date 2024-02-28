"""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
   Se o valor digitado for ímpar, desconsidere-o."""

adicao = 0
for c in range (0, 6):
    num = int(input("Informe um valor inteiro: "))

    if num % 2 == 0:
            adicao = num + adicao       
print("A soma entre os valores pares equivale a {}.".format(adicao))




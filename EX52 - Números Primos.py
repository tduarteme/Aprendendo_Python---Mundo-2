"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

total = 0
lista = []

num = int(input("Digite um número inteiro: "))

for p in range (1, num + 1):
    if num % p ==0:
        total +=1
        lista.append(p)

if total ==2:
    print("O número {} é divisível por \033[1;34m{}\033[m, portanto é PRIMO.".format(num, lista))

else:
    print("O número {} é divisível por \033[1;33m{}\033[m, NÃO É PRIMO!".format(num, lista))
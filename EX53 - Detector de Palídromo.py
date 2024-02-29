"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
    desconsiderando os espaços.

Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA."""


frase = str(input("Digite a frase: ")).strip() .upper()
palavra = frase.split()
junto = "".join(palavra)
invertido = ""

for letra in range (len(junto)-1, -1, -1):
    invertido += junto[letra]

if invertido == junto:
    print("O inverso de \033[1;31m{}\033[m é \033[1;32m{}\033[m".format(junto, invertido))
    print("É PALÍDROMO")

else:
    print("Não é PALÍDROMO")

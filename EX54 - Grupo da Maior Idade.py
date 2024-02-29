"""Crie um programa que leia o ano de nascimento de sete pessoas. 
    No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

from datetime import date
ano = date.today().year

total_maior = 0
total_menor = 0

for pessoas in range(1, 8):
    nascimento = int(input("Digite o ano de Nascimento: "))
    idade = (ano - nascimento)
   
    if idade >= 18:
        total_maior += 1      

    else:
        total_menor += 1 
      
print("Ao todo, tivemos {} pessoas maiores de Idade".format(total_maior))
print("Ao todo, tivemos {} pessoas menores de Idade".format(total_menor))


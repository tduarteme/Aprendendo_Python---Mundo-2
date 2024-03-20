"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
    Caso esteja errado, peça a digitação novamente até ter um valor correto."""

people = str(input("Informe seu SEXO [F] ou [M]: ")).upper()[0]

while people not in "MF":
    people = str(input("Dado incorreto, informe seu Sexo: ")).upper()[0]

print("Sexo {}, registrado!" .format(people))



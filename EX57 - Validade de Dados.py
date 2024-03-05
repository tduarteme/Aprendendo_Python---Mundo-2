"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
    Caso esteja errado, peça a digitação novamente até ter um valor correto."""

people = str(input("Informe seu SEXO [F] ou [M]: ")).strip() .upper()[0]

while people not in "mMfF":
    people = str(input("Sexo errado, informe seu Sexo: ")).strip() .upper() [0]

print("Sexo {}, registrado!" .format(people))



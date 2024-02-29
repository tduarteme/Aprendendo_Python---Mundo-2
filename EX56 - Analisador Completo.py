"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
    a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""

sumidade = 0
media = 0
oldestman = 0
woman20 = 0
oldestname = ""

for people in range (1, 5):
    print("==+== {}ª PESSOA ==+==".format(people))
    name = str(input("NOME: ")) .strip()
    age = int(input("IDADE: "))
    sexo = str(input("F/M: ")) .strip()
    sumidade += age

    if people ==1 and sexo in "Mm":
        oldestman = age
        oldestname = name

    if sexo in "Mm" and age > oldestman:
            oldestman = age
            oldestname = name

    if sexo in "Ff" and age < 20:
                woman20 += 1

media = sumidade / 4
print("A média de idade do Grupo é de {} anos".format(media))
print("O homem mais experiênte tem {} anos e se chama {}".format(oldestman, oldestname))
print("Total de {} mulheres com menos de 20 anos".format(woman20))



  
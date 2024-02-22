"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, 
   de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER """

from datetime import date
ano_nasci = int(input("Informe o ano de Nascimento: "))
ano_atual = date.today().year

idade = (ano_atual - ano_nasci)

print("Sua idade é de {} anos ...".format(idade))

if idade <=9:
    print("Você disputará na categoria MIRIM!!")

elif idade <=14:
    print("Você disputará na categoria INFANTIL!!")

elif idade <=19:
    print("Você disputará na categoria JÚNIOR!!")

elif idade <=25:
    print("Você disputará na categoria SÊNIOR!!")

elif idade >25:
    print("Você disputará na categoria MASTER!!")

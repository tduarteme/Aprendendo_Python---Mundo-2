""" Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade.
Se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date
ano = int(input("Informe o ano de Nascimento: "))
hoje = date.today().year

alistamento = (hoje - ano)


if alistamento == 18:
    print("Sua idade atual é de {} anos é hora alistar, ASPIRA!!!!".format(alistamento))

elif alistamento < 18:
    falta = 18 - alistamento
    print("Você tem {} anos, faltam {} anos para completar 18 anos. Calma, ainda não chegou a hora! ".format(alistamento, falta))

else:
    passou = alistamento - 18
    print("Já tem {} anos, ultrapassou {} anos. Corre, tá atrasado Aspita!!!".format(alistamento, passou))


    
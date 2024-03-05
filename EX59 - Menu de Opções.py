"""Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso."""

from time import sleep
n1 = int(input("Primeiro Valor: "))
n2 = int(input("Segundo Valor:  "))
options = 0

while options != 5:
    print (""" 
    \033[1;33m
          [1] ADIÇÃO
          [2] MULTIPLICAÇÃO
          [3] MAIOR
          [4] NOVOS NÚMEROS
          [5] SAIR
      
        \033[m """)
    options = int(input("Escolha a Opção Desejada: "))

    if options == 1:
        sum= n1+n2
        print("A soma entre {} + {} = {}" .format(n1,n2,sum))

    elif options == 2:
        multi = n1*n2
        print("A multiplicação entre {} * {} = {}".format(n1,n2,multi))

    elif options == 3:
        if n1 > n2:
            maior = n1
            print("O maior é {}".format(maior))
        else:
            maior = n2
            print("O maior é {}" .format(maior))
        
    elif options == 4:
        print("Informe os valores novamente ...")
        n1 = int(input("Primeiro Valor: "))
        n2 = int(input("Segundo Valor:  "))

    elif options == 5:
        print("Saindo ...")
        sleep(2)

    else:
        print("Opção inválida")

print("\033[0;37;40mTérmino do Programa, volte sempre!!!\033[m")

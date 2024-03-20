""" Escreva um programa que leia um número N inteiro qualquer.
    Mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
    Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8 """

numero = int(input("Quantos termos deseja mostrar? "))
primeiro_termo = 0
segundo_termo = 1

print("{} → {}" .format(primeiro_termo, segundo_termo), end=" ")
contador =3

while contador <=numero:

    terceiro_termo = (primeiro_termo + segundo_termo)

    print("→ {}".format(terceiro_termo), end=" ")
    
    primeiro_termo = segundo_termo
    segundo_termo = terceiro_termo
    contador += 1

print("→ FIM")



    


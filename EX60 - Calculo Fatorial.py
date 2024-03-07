""" Faça um programa que leia um número qualquer e mostre o seu fatorial. 
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120"""

###from math import factorial
##numero = int(input("Digite um número, saber saber seu Fatorial: "))
#resultado = factorial(numero)
#print(resultado)

"""A maneira acima, também está correta. 
Entretanto, apenas a forma de como é mostrado o resultado será diferente, veja abaixo o outro método!"""

# Feito com while
numero = int(input("Digite um número, saber saber seu Fatorial: "))
c = numero
fact = 1

print("Calculando {}!=" .format(numero), end=" ")
while c > 0:
    print("{}" .format(c), end=" ")
    print("X" if c > 1 else " = ", end= " ")
    fact*=c
    c-=1

print("{}" .format(fact))



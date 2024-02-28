"""Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ESCALENO: todos os lados diferentes

– ISÓSCELES: dois lados iguais, um diferente

Obs.: Só é possível formar um triângulo, se a soma entre dois segmentos forem menor do que o terceiro."""

from time import sleep
r1 = float(input("Primeiro Segmento: "))
r2 = float(input("Segundo Segmento: "))
r3 = float(input("Terceiro Segmento: "))

print("CALCULANDO ...")
sleep(2)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Esses segmentos foram um TRIÂNGULO, ", end=" ")

if r1 == r2 == r3:
    print("EQUILÁTERO!")

if r1 != r2 != r3 != r1:
    print("ESCALENO!")

elif r1==r2 !=r3 or r2==r1 !=r3 or r3==r1 !=r2:
    print("ISÓSCELES!")

    # Na linha acima (30), eu poderia pôr um ELSE, porém eu quis fazer a lógica.

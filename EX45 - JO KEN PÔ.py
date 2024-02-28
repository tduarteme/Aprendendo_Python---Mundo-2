"""Crie um programa que faça o computador jogar Jokenpô com você."""

from random import randint
from time import sleep

itens = ("PAPEL","PEDRA","TESOURA")
print("""Suas opções: 
      
      [0] - PAPEL
      [1] - PEDRA
      [2] - TESOURA """)

jogador = int(input("Informe a opção desejada: "))
computador = randint(0,2)

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(1)

print("-=*"*20)

if computador == 0: # Computador Jogou Papel.
    if jogador == 0:
        print ("EMPATE")

    elif jogador == 1:
        print ("COMPUTADOR venceu, escolheu {}".format(itens[computador]))
        print ("Jogador jogou, {}" .format(itens[jogador]))

    elif jogador == 2:
        print ("JOGADOR venceu, escolheu {}".format(itens[jogador]))
        print ("Computador jogou, {}" .format(itens[computador]))

    else:
        print ("JOGADA INVÁLIDA")


elif computador == 1: # Computador Jogou, Pedra.
    if jogador == 0:
        print ("JOGADOR venceu, escolheu {}." .format(itens[jogador]))
        print ("Computador perdeu, {}!" .format(itens[computador]))

    elif jogador == 1:
        print ("EMPATE")

    elif jogador == 2:
        print ("COMPUTADOR venceu, escolheu {}." .format(itens[computador]))
        print ("Jogador perdeu, {}!" .format(itens[jogador]))

elif computador == 2: # Computador Jogou, Tesoura.
    if jogador == 0:
        print ("COMPUTADOR venceu, escolheu {}.".format(itens[computador]))
        print ("Jogador perdeu, {}!" .format(itens[jogador]))

    elif jogador == 1:
        print("JOGADOR venceu, escolheu {}." .format(itens[jogador]))
        print ("Computador perdeu, {}!" .format(itens[computador]))

    elif jogador == 2:
        print ("EMPATE")

    else:
        print("JOGADA INVÁLIDA")

print("-=*"*20)
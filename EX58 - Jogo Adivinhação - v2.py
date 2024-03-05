"""Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
   Só que agora o jogador vai tentar adivinhar até acertar.
   Mostrando no final quantos palpites foram necessários para vencer."""

from random import randint
print ("Tente adivinhar o número que o computador está pensando, entre 0 e 10: ")
computador = randint (0, 10)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input("Vamos lá!!! Qual o seu Palpite? "))
    palpites += 1

    if jogador == computador:
        acertou = True

    else:     

        if jogador < computador:
            print("Mais!!! Tente outra vez, não desista.")
    

        elif jogador > computador:
            print("Menos!!! Tente outra vez, não desista.")

print("Caramba, você precisou de {} tentativas para acertar!!" .format(palpites))
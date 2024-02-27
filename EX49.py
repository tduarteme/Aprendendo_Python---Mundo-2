"""Desenvolva uma solução mostrando a tabuada de um número que o usuário escolher, 
   só que agora utilizando um laço for."""

tabuada = int(input("Tabuada e de qual número? "))

for t in range (1, 11):
    multi = tabuada * t    
    print("{} X {} = {}".format(tabuada, t, multi))
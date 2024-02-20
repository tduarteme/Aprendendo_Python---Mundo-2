""""Crie um programa que leia duas notas de um aluno e calcule sua média.
    Mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO """


n1 = float(input("N1: "))
n2 = float(input("N2: "))

media = (n1+n2) /2

if media >=7:
    print("Parabéns APROVADO! Sua média foi {:.1f} passou de série.".format(media))

elif media < 5:
    print("Que pega, sua média foi {:.1f}. REPROVADO, estude mais!".format(media))

elif 7> media >=5:
     print("Sua média foi {:.1f}. RECUPERAÇÃO!!!".format(media))


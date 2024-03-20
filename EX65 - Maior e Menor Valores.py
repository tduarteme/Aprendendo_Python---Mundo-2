"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
   O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

r = "S"
cont = media = soma = 0

while r == "S":
    n1 = int(input("Digite um número: "))    
    cont +=1
    soma +=n1

    if cont ==1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
        
    r = str(input("Deseja continuar [S/N]: ")).strip() .upper()[0]
media = soma / cont
print ("Você digitou {} números e média entre eles equivale a {}." .format(cont, media))
print ("O maior número foi {} e o menor {}." .format(maior, menor))

print("→ FIM")

    
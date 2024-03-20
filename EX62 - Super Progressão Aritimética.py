"""Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
    O programa encerrará quando ele disser que quer mostrar 0 termos."""

print("=-*"*20)
print("TERMOS DE UMA PA")
print("=-*"*20)


primeiro = int(input("Primeiro Termo: "))
razao = int (input("Digite a Razão: "))
termo = primeiro
contador = 1
total = 0
plus = 10

while plus != 0:
    total = total + plus

    while contador <=total:
        print("{} ->" .format(termo), end=" ")
        termo = termo + razao # O cálculo pode ser feito assim.
        contador += 1 # Ou dessa maneira também
    print("PAUSE")
    plus = int(input("Quantos mais termos, deseja? "))

print("FINISH")
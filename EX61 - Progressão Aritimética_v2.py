"""Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA.
   Mostrando os 10 primeiros termos da progressão usando a estrutura while."""

print("=-*"*20)
print("10 TERMOS DE UMA PA")
print("=-*"*20)


primeiro = int(input("Primeiro Termo: "))
razao = int (input("Digite a Razão: "))
termo = primeiro
decimo = 1

while decimo <=10:
    print("{} ->" .format(termo), end=" ")
    termo = termo + razao # O cálculo pode ser feito assim.
    decimo += 1 # Ou dessa maneira também

print("FINISH")
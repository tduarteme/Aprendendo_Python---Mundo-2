print("=-*"*20)
print("10 TERMOS DE UMA PA")
print("=-*"*20)

termo = int(input("Primeiro Termo: "))
razao = int (input("Digite a Razão: "))
decimo = termo + (10-1) * razao

for c in range (termo, decimo + razao, razao):
    print(c, end= " -> ")
print("FINISH")
""" Escreva um programa em Python que leia um número inteiro qualquer e 
    peça para o usuário escolher qual será a base de conversão: 
    1 para binário, 2 para octal e 3 para hexadecimal."""

numero = int (input("Digite um valor inteiro: "))

print ("[1] Conversão em BINÁRIO")
print ("[2] Conversão em OCTAL")
print ("[3] Conversão em HEXADECIMAL")

opcao = int(input("Informe sua opção: "))

if opcao == 1:
    print("O valor convertido em BINÁRIO é {}.".format(bin(numero)[2:]))

elif opcao == 2:
    print("O valor convertido em OCTAL é {}.".format(oct(numero)[2:]))

elif opcao == 3:
    print("O valor convertido em HEXADECIMAL é {}.".format(hex(numero)[2:]))

else:
    print("Opção inválida, por favor tente novamente!")
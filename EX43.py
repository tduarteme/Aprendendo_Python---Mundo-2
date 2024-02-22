"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e 
   mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida """

peso = float(input("Informe o Peso : "))
altura = float(input("Informe a altura: "))

imc = peso/(altura*altura)

if imc < 18.5:
    print("Abaixo do Peso")

elif 18.5<= imc <=25:
    print("Parabéns, peso IDEAL!")

elif 25<= imc <30:
    print("Atenção, você está em SOBREPESO!")

elif 30<= imc <40:
    print("Eita, você está OBESO cuide-se!")

else:
    print("PERIGOO, obesidade mórbita, procure um médico!!!")
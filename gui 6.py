#solicita os dados do usuário 
nome = input(" digite seu nome: ")
peso = float(input("digite seu peso (em kg:)"))
altura =float(input("digite sua altura (em metro): "))


# calcule do IMC
imc =peso / (altura* altura)

# exibe o resultado imc
print(f"\n{nome}, seu imc é: {imc:.2f}")

#classificação com base no vallor do IMC
if imc < 18.5:
   print("classificação: Abaixo do peso.")
elif imc >= 18.5 and imc <= 24.9:
  print("classificacação: peso normal.")
elif imc >= 25.0 and imc <= 29.9:
    print("classicação: sobrepeso.")
else: #IMC >= 30.0
    print("classificação: obsidade.")  
 
 
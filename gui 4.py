# inicialização da variável opção
opção = -1 # começa com valor diferente de 0 para entrar no loop

# loço principal
opção = int(input("escolha uma opção: "))

if opção == 1 or opção == 2 or opção == 3 or opção == 4:
    num1 = float(input("digite o primeiro número: "))
    num2 =float(input("digite o segundo múmero"))
    
if opção == 1:
    resultado = num1 + num2 
    print(f"Resultado da soma :{resultado}")
elif opção ==2:
    resultado =num1 - num2
    print(f"resultado da subtração: {resultado}")
elif opção ==3:
    resultado = num1 * num2
    print(f"resultado de multiplicação: {resultado}")
elif opção ==4:
    if num2 != 0:
     resultado = num1 / num2
     print(f"resultado da divisão: {resultado}")
    else:
     print("erro: divisão por zero não é permitida.")
elif opção == 0:
   print("calculadora encerrada. ")
else:
    print("opção inválida. tente novamente.")   
    
    
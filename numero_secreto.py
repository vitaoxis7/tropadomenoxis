import random
numero_secreto= random.randint (1,10)
tentativa =0
contagem_tentativa=0
print("bem vindo ao jogo secreto==")
print("tente adivinha o numero secreto entre 1 a 10")
while tentativa != numero_secreto:
    numero= int(input("digite um numero: "))
    contagem_tentativa= contagem_tentativa+1
    if numero== numero_secreto:
        print("parabens você acertou o numero secreto")
        print(f"você precisou de {contagem_tentativa} tentativas")
        break
    elif numero< numero_secreto:
        print("o numero secreto e maior")
    else:
        print("o numero secreto e menor")
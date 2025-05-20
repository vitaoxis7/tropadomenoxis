
km = float(input("digite a quantidade de KM percorridos:"))

litros = float (input("digite a quantidade de litro de combustivel consumidos:"))

if litros != 0:
   consumo = km / litros
   print(f"o comsumo médio do carro é de { consumo:.2f}km/L.")
else:
    print("Não é possivel calcular o consumo com 0 litros.")
    print("por favor, digite valores numéricos válidos. ")  
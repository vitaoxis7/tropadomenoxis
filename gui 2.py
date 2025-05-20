# solicitar ao usuário9 o valor total da compra
valor_total = float(input("digite o valor total a compra; R$"))

#calcula o valor de cada uma das 5 prestações (sem juros)
pretacao = valor_total / 5

#Exibe os resuldos
print("\nresumo da compra: ")
print(f"valor total da compra: R$ {valor_total:.2f}")
print("valor de cadda prestações: R$ {prestacao:.2f}")
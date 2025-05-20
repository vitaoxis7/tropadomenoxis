print("\n... tabela de preços ...")
print("valor por dia alugado: R$90.00")
print(" valor por km rodado R$0.20")

# solicitar os dados ao usuário
dias = int(input("\nquantos dias o carro foi alugado"))
kms = float(input("quanto kms foram percorridas"))

# calcule os valores
valor_dias =dias * 90.00
valor_kms =kms * 0.20
total= valor_dias + valor_kms

#exibe o recibo detalhado
print("----recibo do aluguel ---")
print(f"total de dias alugados:{dias} dia(s) - R${valor_dias:.2f}")
print(f"total de kms percorridos: {kms:.2f} km -R${valor_kms:.2f}")
print(f"\nvalor total a pagar: R${total:.2f}")
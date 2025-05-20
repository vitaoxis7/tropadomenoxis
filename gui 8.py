 
    # Declarar variaveis
    numero = 0
    frances = 0
    integral = 0
    doce_liso = 0
    doce_farofa = 0
    forma = 0 
    valor_frances = 1.04
    valor_integral = 1.04
    valor_doce_liso = 1.08
    valor_doce_farofa = 1.11
    valor_forma = 0.95
    valor_total = 0
    while opcao !=6:
        print("-- PADARIA --")
        print("[1] pão françes")
        print("[2] pão integral")
        print("[3] pão doce liso")
        print("[4] pão doce farofa")
        print("[5] pão de forma")
        print("[6] fim da compra")
        opcao = int(input("Escolha sua opção"))
        # casos do sistema 
        if opcao ==1:
            Frances = int(input("Digite a quantidade de pão françes: "))
            valor_total += frances * valor_frances
        elif opcao ==2:
            integral=int(input("Digite a quantidade de pão integral: "))
            valor_total += integral * valor_integral
        elif opcao ==3:
            doce_liso=int(input("Digite a quantidade de pão doce liso: "))
            valor_total += doce_liso * valor_doce_liso
        elif opcao ==4:
            doce_farofa=int(input("Digite a quantidade de pão doce farofa: "))
            valor_total += doce_farofa * valor_doce_farofa
        elif opcao ==5:
            forma=int(input("Digite a quantidade de pão de forma: "))
            valor_total += forma * valor_forma
        elif opcao != 6:
            print("Opção invalida. Tente novamente escolhendo outra opção")
            
    # Recibo
    print("\n-- Recibo --")
    if frances > 0:
        print(f"Pão frances: {frances} unidade x R${valor_frances:.2f} = R${frances*valor_frances:.2f}")
    if integral > 0:
        print(f"Pão integral: {integral} unidade x R${valor_integral:.2f} = R${integral*valor_integral:.2f}")
    if doce_liso > 0:
        print(f"Pão doce liso: {doce_liso} unidade x R${valor_doce_liso:.2f} = R${doce_liso*valor_doce_liso:.2f}")
    if doce_farofa > 0:
        print(f"Pão doce farofa: {doce_farofa} unidade x R${valor_doce_farofa:.2f} = R${doce_farofa*valor_doce_farofa:.2f}")
    if forma > 0:
        print(f"Pão de forma: {forma} unidade x R${valor_forma:.2f} = R${forma*valor_forma:.2f}")
        print(f"Valor total: R${valor_total:.2f}")
    
        
        

opcao = 0
while opcao != 5:
    print ("===Cardapio===")
    print ("1- hamburguer")
    print ("2- pizza")
    print ("3- salada")
    print ("4- refrigerante")
    print ("5- sair")
    opcao = int(input("escolha uma opção: "))
    if opcao ==1:
        print("Você escolheu hamburguer!!")
    elif opcao == 2:
        print("Você escolheu pizza!!")
    elif opcao == 3:
        print("Você escolheu salada!!")
    elif opcao == 4:
        print("Você escolheu refrigerante!!")
    elif opcao == 2:
        print("Saindo do cardapio!!")
        break

def menu(nome_festival):
    opcoes = {
        "1" : "Comprar Ingresso por CPF",
        "2" : "Ver seus ingressos",
        "3" : "Vizualizar ingressos disponiveis",
        "4" : "Ver clientes do Festival",
        "5" : "Sair" 
    }
    while True:
        try:
            print(f" FESTIVAL {nome_festival}".center(40, "-"))
            for v, o in opcoes.items():
                print(f"{v} - {o}")
            valor = input("Sua opcao: \n>>> ")
            if opcoes[valor]:
                return valor
        except:
            print("Opcao invalida.")

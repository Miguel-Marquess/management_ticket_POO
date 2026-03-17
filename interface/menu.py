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

def selecionar_tipo(tipos):
    ingressos = {}
    for p, v in enumerate(tipos, start=1):
        ingressos[p] = v
    print("Selecione um Ingresso".center(40, "-"))
    while True:
         try:
             for p, v in ingressos.items():
                 print(f"{p} - {v[0]} | Preco: {v[1]["preco"]} | Disponivel: {v[1]["quantidade"]}")
             return ingressos[int(input("Digite a posicao: \n>>> "))][0]
         except KeyError:
            print("Digite uma opcao valida.")
         except Exception as e:
             print(e)
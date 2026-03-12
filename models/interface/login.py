def login(festival):
    while True:
        try:
            login = input("Ja tem conta registrada: [S/n] \n>>> ")
            if login == "S":
                cpf = input("Digite seu CPF: \n>>> ")
                senha = input("Digite sua senha: \n>>> ")
                return festival.login(cpf, senha)
                
            elif login == "n":
                nome = input("Digite seu nome: \n>>> ")
                cpf = input("Digite seu CPF: \n>>> ")
                email = input("Digite seu email: \n>>> ")
                senha = input("Digite sua senha: \n>>> ")
                return festival.cadastrar_cliente(nome, cpf, email, senha)
            else:
                print("Digite uma opcao valida.")
        except Exception as e:
            print(e)